# Content page
- [Industry Partner Meeting #1 - Preparation](#Industry-Partner-Meeting-1---Preparation)
- [Industry Partner Meeting #2 - Preparation](#Industry-Partner-Meeting-2---Preparation)
- [Industry Partner Meeting #3 - Preparation](#Industry-Partner-Meeting-3---Preparation)

***
# Industry Partner Meeting #1  - Preparation

## Meeting Date: [19/03/2025]

**Attendees:**
- Hongkun Zhang
- Yifeng Su
- Xiang Zhou
- Yutao Zhou
- Junbo Liamg
- Fabio

## Meeting Agenda
1. **Introduction** (Team introduces themselves and project overview)
2. **Understanding the Industry Partner's Needs**
   - What challenges is the industry partner facing?
   - What are their goals and expectations for this project?
3. **Scope of the Project**
   - What are the key deliverables?
   - Are there any constraints (time, technologies)?
4. **Requirements Elicitation**
   - What functionalities are needed?
   - Are there existing processes or tools we should integrate with?
5. **Next Steps & Action Items**
   - Define clear follow-up actions and deadlines.

## Key Questions to Ask
- What are the most important features for the project?
- Who will be the primary point of contact for feedback?
- Are there any existing documents or workflows we should be aware of?
- What are the success criteria for this project?
- Where does the data come from? (who provides)
- Does the client already have a relevant technical framework that we can build on top of?

## Notes from the Meeting
- Make a chatbot, which can respond the user with the input question according to previous aviation cases
- step 0: analysis narratives, find similar, step 1: gather similar info -> generate instruction, step 2: agent builder

***
# Industry Partner Meeting #2 - Preparation
## Meeting Date: [26/03/2025]

**Attendees:**
- Hongkun Zhang
- Yifeng Su
- Xiang Zhou
- Yutao Zhou
- Junbo Liamg
- Fabio

## Meeting Agenda
1. **Clarify the Industry Partner's Needs by introducing our analyzation and user story**
   - Is our direction correct?
2. **Introduction of the current plan**
   - Does the customer have a preferred solution?
3. **Scope of the Project**
   - Where will the final project be deployed?  
4. **Budget issues**
   - Is there any funding available?
5. **Next Steps & Action Items**
   - Define clear follow-up actions and deadlines.

## Key Questions to Ask
- Is our direction correct based on the user story?
- Define clear follow-up actions and deadlines.
- Is there any funding available?
- Where will the final project be deployed?  

## Notes from the Meeting
  - User stories are good and acceptable.
  - Data is open sources.
  - Purpose of this product: user prompt and chatbot generate a scenario and engage conversation with user, focus on the learning outcome of the user, more like a learning software.
  - Clients could provide us some typical questions and answers.
  - There are many dataset available, can be included in the furthur stage.
  - Do the no server and no paid LLM approach.

***

# Industry Partner Meeting #3 - Preparation

## Meeting Date: [23/04/2025]

**Attendees:**
- Hongkun Zhang
- Yifeng Su
- Xiang Zhou
- Yutao Zhou
- Junbo Liamg
- Fabio

## Meeting Agenda
1. ‎**Reporting the progresses** (10-15 min)
    - What we worked on in sprint1.
    - What we are going to accomplish in sprint 2.
    - What we have done in sprint 2.
2.  **Feedback from client** (10-15 min)

## Sprint1 progresses
- **Clarified the project Goal & Scope.**
  - CRMSON chat-bot for training and review the incidents in high-risks environment.
  - In-scope feature & out-scope feature: such as focus on communication breakdowns but not technical issues.
- **Personas and Motivational Model.**
  - We analysed the potential users from the given dataset and derived several personas.
  - For example, the flight attendant Olivia.
    - Goals: Ensure the safety and comfort of all passengers
    - Pain Points: Confrontations with passengers who violate regulations
    - Interaction with the System: She is eager to use CRMSON to simulate potential conflict scenarios, improve her communication approach, and avoid escalating conflicts while ensuring safety protocols are upheld.
- **User stories.**
  - We derived 4 epic user stories from the personas. Assigning them priority and breaking down to small user stories with story points.
  - Mapping the user stories to sprints.
  - In sprint 2 we are working on some of the user stories which are “must have”.
- **Prototyping.**
  - We have a brief idea about how CRMSON chat-bot will interact with the user.
  - Currently in sprint2 we are optimizing the workflow of this prototype, which will be introduced later.

## Sprint 2 objective
1. **Initial Application Entry Point.**
    - We might develop a simple UI for this or using the UI provided from the platform.
2. **Input Conflict Scenario.**
    - User can key in their desired scenario, then AI will analyse it.
3. **Retrieve Similar Case Suggestions.**
    - AI search the database and find the most similar case and then present to the user.
4. **Multi-turn Conversation Simulation.**
    - After user selected the scenario, then start simulating.

Basically, by the end of sprint 2, we can have a demo that only for communication breakdown, and only able to simulate for the role of flight attendant.
We want to finish the smallest unit of this chat-bot and see how it go, then either modifying or scaling it up would be easier.

## Sprint2 progresses
- **Data cleaning.**
  - Select only the records that are communication breakdown and happen between flight attendant and other people.
  - Dropped the useless fields.
  - Use model to transform the first-person narrative into an objective summary of the third-person narrative
  - Use model to analyse all the records and assigned labels to each record (with this customised and specific label might increase the precision of chat-bot to find the similar scenario).
  - Each label with a corresponding csv file and containing all records with this label. Easy for the model to search.
- **Model selection.**
  - Read through the report about those open source LLMs, overall, Llama is the outperformed. 
  - We are trying to deploy it on our device, as well as trying to use it from the online platform such as Hugging face. Need to compare how do these two go with our design.
- **Platform selection.**
  - We found a powerful platform that suitable for our project, since it allows more customised functionality in using the mode.

