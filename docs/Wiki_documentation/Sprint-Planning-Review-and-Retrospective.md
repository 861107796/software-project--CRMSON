# Sprint 1 Planning

## Sprint Details
- **Sprint Number**: [Sprint #1]
- **Start Date**: [2025-3-14]
- **End Date**: [2025-4-4]
- **Sprint Goal**: Clarify customer needs and project direction, determine the technology stack to be used, and prepare for subsequent model deployment and training.

---

## Sprint Backlog

| User Story / Task                           | Description                                                                                                                | Status |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|--------|
| Client Interviews & Requirement Gathering   | Communicate with the client to collect and confirm project requirements, and understand business goals and pain points    | Done   |
| Define Project Scope & Direction            | Clarify project objectives and scope based on requirements, and define deliverables                                       | Done   |
| Technical Feasibility Assessment            | Research and evaluate potential models, tools, and frameworks; confirm deployment environment                              | Done   |
| Finalize Tech Stack                         | Decide on the main technologies for model training and deployment (e.g., PyTorch, FastAPI)                                 | Done   |
| Data Requirements Analysis                  | Identify the data types and formats needed for training; assess availability of existing data                              | Done   |
| Initial Model Architecture Design           | Design initial model architecture, flowchart, and module breakdown to prepare for development                              | Done   |
| Sprint Review Preparation                   | Summarize Sprint outcomes and prepare presentation materials for the review meeting                                        | Done   |

---

# Sprint 1 Review

**Sprint Number**: [Sprint #1]  
**Duration**: 2025-3-14 ～ 2025-4-4  
**Sprint Goal**: Clarify customer needs and project direction, determine the technology stack to be used, and prepare for subsequent model deployment and training.

---

## Summary of Accomplishments

1. **Client Interviews & Requirement Gathering**  
   - Conducted multiple sessions with the client to fully understand their business goals and training scenarios.  
   - Collected initial requirements for user flow, training objectives, and system performance expectations.

2. **Define Project Scope & Direction**  
   - Consolidated client interview findings into a formal project scope.  
   - Ensured team alignment on overall objectives, phased milestones, and next steps.

---

## Items In Progress

1. **Technical Feasibility Assessment**  
   - Completed initial research on potential LLM-based solutions and frameworks.  
   - Shortlisted candidate models (e.g., GPT-based, other open-source LLMs), pending further performance/resource verification.

2. **Finalize Tech Stack**  
   - Narrowed down libraries (e.g., PyTorch) and frameworks (e.g., FastAPI or Flask) for the backend.  
   - Considering deployment options (on-prem vs. cloud) and assessing budget implications.

3. **Data Requirements Analysis**  
   - Documented the types of conflict scenarios needed (e.g., passenger misconduct, emergencies).  
   - Awaiting clarity on data format, volume, and availability from the client side.

4. **Initial Model Architecture Design**  
   - Drafted a high-level design showing user input, scenario retrieval, and multi-turn interactions.  
   - Awaiting final feasibility results to confirm the model pipeline approach.

5. **Sprint Review Preparation**  
   - Consolidated notes and key findings from Sprint 1 for review with stakeholders.

---

## What Went Well

- **Active Stakeholder Engagement**: The client provided prompt feedback and clear priorities.  
- **Better Understanding of the Problem**: The team now has a solid grasp on core training needs and typical conflict scenarios.

---

## Challenges

- **Tech Stack Uncertainty**: Ongoing comparison between open-source and proprietary solutions.  
- **Data Availability**: Some data remains confidential or unconfirmed, delaying final decisions about data structure and usage.

---

## Next Steps / Recommendations

1. **Complete Technical Feasibility Testing**  
   - Prototype experiments with shortlisted models to finalize the core technology stack and confirm resource requirements.

2. **Lock Down Data Strategy**  
   - Confirm data collection methods, format, and any necessary approvals for using real incident data.

3. **Refine Model Architecture**  
   - Incorporate feasibility testing outcomes into the initial architecture design.

4. **Plan Sprint 2**  
   - Focus on Must Have user stories (scenario input, retrieval, multi-turn conversations) for a functional first version.

---

# Sprint 2 Planning

## Sprint Details
- **Sprint Number**: [Sprint #2]
- **Start Date**: [2025-4-5]
- **End Date**: [2025-5-2]
- **Sprint Goal**: Deliver the core (Must Have) features for inflight conflict simulation, ensuring a basic end-to-end flow: from scenario input to multi-turn conversation.

---

## Sprint Backlog

| User Story / Task                                   | Description                                                                                                                                                      | Status |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| **US2.1 – Input Conflict Scenario**                 | Provide a basic interface/terminal for flight attendants to enter conflict scenario descriptions, ensuring the system can capture and process this information. | Done |
| **US2.3 – Retrieve Similar Case Suggestions**       | Implement a mechanism to display relevant past cases based on the input scenario, giving flight attendants useful references before starting simulations.        | Continue |
| **US2.5 – Multi-turn Conversation Simulation**      | Integrate the LLM/chat engine for realistic multi-turn conversations that maintain context, forming the core of inflight conflict simulation.                   | Done |
| **Integration & Testing**                           | Perform end-to-end tests to ensure scenario input, case retrieval, and multi-turn conversation function together smoothly, addressing any major bugs.            | Done |
| **Sprint Review Preparation**                       | Summarize this Sprint’s deliverables, demo the functional flow (input → retrieve → simulate), and prepare review materials.                                      | Done |

---

# Sprint 2 Review

**Sprint Number**: [Sprint #2]  
**Duration**: 2025-4-5 ～ 2025-5-2  
**Sprint Goal**: Create a prototype system, which includes basic functions such as multi-round interaction, input, and evidence retrieval.

---

## Summary of Accomplishments

1. **Determine deployment method & LLM selections**
   - Used the Dify platform and design our own workflow to guide the flow of the application.
   - Text analysis was performed using llama-3 and case retrieval was performed using QWEN-embedding.

2. **Initial Application Entry Point & Input Conflict Scenario**  
   - Used the default UI of the Dify platform for input, we will develop our own featured UI in future sprints.
   - A LLM was implemented to analyze the key information in the user input.

3. **Retrieve Similar Case & Multi-turn Simulation**  
   - Used word embedding methods to search for the closest scenarios.
   - The conversation will continue until the user prompts the chatbot to stop.

---

## Sprint 2 Burndown Chart

![17a8b5210e02b0ea0bf59b36bc551cc](https://github.com/user-attachments/assets/e18b2490-45e9-4ad6-aad1-116bff86b2f7)

***

## Items In Progress

1. **Data Cleaning**  
   - Select only the records that are communication breakdown and happen between flight attendant and other roles.
   - Dropped the useless fields.
   - Use model to transform the first-person narattive into an objective summary of the thrid-person narrative.
   - Use model to analyse all the records and assigned labels to each records (with this customised and specific label might increase the precision of chat-bot in finding the similar scenario).
   - Each label with a corresponding csv file and containing all records with this label.


2. **Model selection**  
   - Read through the report about those open source LLMs, overall, Llama is the outperformed.
   - We are trying to deploy it on our device, as well as trying to use it from the online platform such as Hugging face, depend on how these two are performed.

3. **Platform selection**  
   - We decided to use the Dify platform for our project, since it allows more customized functionality in using the model.

4. **Sprint Review Preparation**  
   - Consolidated notes and key findings from Sprint 2 for review with stakeholders.

---

## What Went Well

- **Active Stakeholder Engagement**: We present our progresses from sprint 2 to the client, and actively accepted the feedbacks.
- **Better use of development tools**: We are more familiar with managing GitHub kanban boards and developing version control.

---

## Challenges

- **Accuracy of Retrieval**: The accuracy of retrieving the most similar cases is still not high.
- **Chatbot's intelligence isn't enough**: The interactions with chatbots still cannot be used for training purposes.

---

## Next Steps / Recommendations
1. **US2.2 – Select the Role in Simulation**
    - Continue development to allow users to choose chatbot or user roles dynamically through the UI interface, supporting context-appropriate thinking.
2. **US2.3 – Retrieve Similar Case Suggestions**
    - Further refine the case retrieval mechanism, improving matching accuracy based on input scenario descriptions.
3. **US2.4 – Choose to View Case or Skip**
    - Develop and integrate the intermediate step after retrieval for users to preview suggested cases or skip directly into simulation.
4. **US2.6 – Vary Emotional Tone of Passenger**
    - Build initial logic allowing the chatbot to simulate a range of emotional tones from cooperative to disruptive behaviors.
5. **US2.7 – Restart Simulation with New Strategy**
    - Prototype functionality for users to reset and restart the same scenario with a modified chatbot role or emotional tone.
6. **US2.10 – Initial Application Entry Point**
    - Build a working UI for scenario input, case retrieval, and role selection, connecting to core backend simulation features.
7. **Integration & Testing**
    - Perform unit test to each individual feature and begin integration testing of the multiple features above to ensure smooth transition.
8. **Sprint Review Preparation**
    - Prepare deliverables for the sprint3 demo, including role and tone selection → input scenario → retrieve → simulate → restart simulation flow.

---

# Sprint 3 Planning

## Sprint Details
- **Sprint Number**: [Sprint #3]
- **Start Date**: [2025-5-3]
- **End Date**: [2025-5-30]
- **Sprint Goal**: Deliver the auxiliary (Should Have & Could have) features for inflight conflict simulation, ensuring a complete end-to-end flow: from role play selection and change the tone to simulate again.

---

## Sprint Backlog

| User Story / Task                                   | Description                                                                                                                                                      | Status |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| **Study the front-end related knowledge** | Ensure that customized UI can be developed successfully. | To Do |
| **US2.2 - Select the role in simulation**                 | Enable role-playing in the chatbot via UI interface, help it think about responses appropriate to its role, and allow switching roles between the chatbot and the user. | To Do |
| **US2.3 – Retrieve Similar Case Suggestions**       | Implement a mechanism to display relevant past cases based on the input scenario, giving flight attendants useful references before starting simulations.        | Continue |
| **US2.4 - Choose to view case or skip**      | A function between the completion of the database search and the start of the simulation session, it allows the user to check whether this is the situation that he wants to simulate. | To Do |
| **US2.6 - Vary emotional tone of passenger**        | Allows chatbots to simulate personality attitudes ranging from cooperative to annoying. | To Do |
| **US2.7 - Restart simulation with new strategy**        | Allow users to repeat the same scenario by changing the chatbot’s tone and role. | To Do |
| **US2.10 – Initial Application Entry Point**        | Create a minimal UI or CLI tool for interacting with the chatbot, allowing for scenario input and role selection.                                               | To Do |
| **Integration & Testing V2**                           | Perform end-to-end tests to ensure role-palying, more accurate case retrieval, dynamic simulating stategy and functions together smoothly, addressing any major bugs. | To Do |
| **Sprint Review Preparation**                       | Summarize this Sprint’s deliverables, demo the complete functional flow (role & tone selection → input → retrieve → simulate → role & tone selection → simulate again), and prepare review materials.                                      | To Do |

---

# Sprint 3 Review

**Sprint Number**: [Sprint #3]  
**Duration**: 2025-5-3 ～ 2025-5-30  
**Sprint Goal**: Improve auxiliary functions for in-flight conflict simulation and implement a complete end-to-end process: from role-playing selection and changing tone to re-simulation. Deploy the backend in MRC and connect it with the frontend, and realize a more improved frontend code.

---

## Summary of Accomplishments

1. **Update the original version 1 model to version 2**
   - Updated retrieval logic from a fixed 18-document list to a full semantic knowledge base.
   - Improved retrieval accuracy to support better simulation and enable upcoming advanced features.

2. **Adding new features to the model**  
   - Case Selection: Users can now choose one of the top 3 most similar historical scenarios for simulation.
   - Role Selection: Each case contains two roles; users can pick one and the model will simulate the other.
   - Tone Selection: Allows users to define the tone intensity (e.g., polite, emotional) of the simulated conversation.

3. **Frontend and Backend Integration**
   - Developed and deployed a user-friendly Gradio-based frontend, now fully connected to the backend hosted on MRC.
   - Ensured the frontend supports dynamic input, role/tone selection, and renders multi-turn dialogue smoothly.

4. **Robustness and Performance Enhancements**
   - Optimized backend logic to handle unexpected or malformed inputs more gracefully.

   - Fine-tuned the model for more coherent and realistic multi-turn conversations.
5. **Pending Work**
   - ❌ User Guidance Feature: Intended to provide recommended responses for trainees based on best practices, but this feature is still pending due to the lack of labeled ground truth data.

---

## What Went Well

- **Successful Frontend Deployment**: Smooth integration of Gradio with MRC-hosted backend.
- **Improved User Interaction**: Tone, role, and case selection greatly improved realism and flexibility.
- **Robustness**: Backend handles unexpected input reliably without breaking.

---

# Sprint 4 Planning

## Sprint Details
- **Sprint Number**: [Sprint #4]
- **Start Date**: [2025-5-31]
- **End Date**: [2025-6-13]
- **Sprint Goal**: Improve all documentation, organize the entire project, and complete the delivery task.

---