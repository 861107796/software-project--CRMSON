import os
import gradio as gr
from dotenv import load_dotenv
import requests
import json
import time

load_dotenv("api-key.env")
DIFY_API_KEY = os.getenv("DIFY_API_KEY")
DIFY_ENDPOINT = "http://localhost:8080/v1/chat-messages"

headers = {
    "Authorization": f"Bearer {DIFY_API_KEY}",
    "Content-Type": "application/json"
}

def disable_buttons():
    return gr.update(interactive=False), gr.update(interactive=False)

def enable_buttons():
    return gr.update(interactive=True), gr.update(interactive=True)


def chat_simulation_send_user_input(user_input, history):
    history.append({"role": "user", "content": user_input})
    return history, "", user_input

def clear_all():
    return [], None, "Flight Attendant", "", []

def chat_simulation_stream_reply(history, conv_id, role, user_input):
    user_input = user_input.strip()
    if not user_input:
        history.append({"role": "assistant", "content": "(Error: input is empty)"})
        yield history, history, conv_id
        return

    is_first_turn = sum(1 for msg in history if msg["role"] == "user") == 1
    full_input = f"Hi, I am a {role}. {user_input}" if is_first_turn else user_input

    payload = {
        "inputs": {},
        "query": full_input,
        "response_mode": "blocking",
        "user": "abc-123"
    }

    print(payload["query"])

    if conv_id:
        payload["conversation_id"] = conv_id

    try:
        response = requests.post(DIFY_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        reply = data.get("answer", "(No answer)")
        new_conv_id = data.get("conversation_id", conv_id)

        history.append({"role": "assistant", "content": ""})
        for char in reply:
            history[-1]["content"] += char
            time.sleep(0.01)
            yield history, history, new_conv_id

    except Exception as e:
        reply = f"(Error: {str(e)})"
        history.append({"role": "assistant", "content": reply})
        yield history, history, conv_id


# Gradio UI
with gr.Blocks(css="""
/* background */
body, .gradio-container {
    background-color: #001f3f !important;
}
/* message color */
.message.user, .gr-chat-message.user {
    background-color: #8B0000 !important;
    color: white !important;
}
.message.user *, .gr-chat-message.user * {
    color: white !important;
}
/* bot message color */
.message.assistant, .gr-chat-message.assistant {
    background-color: #555555 !important;
    color: white !important;
}
.message.assistant *, .gr-chat-message.assistant * {
    color: white !important;
}
/* button */
#send-btn, #clear-btn {
    background-color: #d4af37 !important;
    color: black !important;
}
""") as demo:

    gr.Markdown("<h2 style='text-align: center; color: white;'> CRMSON Chat Bot </h2>")

    with gr.Row():
        role_dropdown = gr.Dropdown(
            choices=["Flight Attendant", "Airline Captain", "Maintenance Technician"],
            value="Flight Attendant",
            label="Select Your Role"
        )

    chatbot = gr.Chatbot(label="Simulation Chat", type="messages")
    history_state = gr.State([])
    conversation_id_state = gr.State(None)
    user_input_cache = gr.State("")

    user_input = gr.Textbox(placeholder="Describe the situation you're handling...", label="Your Input")
    send_btn = gr.Button("Send", elem_id="send-btn")
    clear_btn = gr.Button("Clear All", elem_id="clear-btn")


    send_btn.click(
        fn=disable_buttons,
        outputs=[send_btn, clear_btn]
    ).then(
        chat_simulation_send_user_input,
        inputs=[user_input, history_state],
        outputs=[chatbot, user_input, user_input_cache],
        queue=False
    ).then(
        chat_simulation_stream_reply,
        inputs=[history_state, conversation_id_state, role_dropdown, user_input_cache],
        outputs=[chatbot, history_state, conversation_id_state],
        queue=True
    ).then(
        fn=enable_buttons,
        outputs=[send_btn, clear_btn]
    )


    clear_btn.click(
        fn=clear_all,
        inputs=[],
        outputs=[chatbot, conversation_id_state, role_dropdown, user_input, history_state]
    )

demo.launch()
