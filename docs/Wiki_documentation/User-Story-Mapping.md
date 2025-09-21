## User Story Decomposition
### Justification
  - We are currently in the early stages and only support flight attendant scenario simulations as our start point
## User Story 2 Decomposition
### Epic: Inflight Conflict Simulation
### User Story Point: 1 point per day per people
| Decomposited User Story ID | As a             | I want to                                             | So that                                                                 | Priority     |Story Points | Justification                        |
|----------------------------|------------------|--------------------------------------------------------|-------------------------------------------------------------------------|--------------|------------------|--------------------------------------|
| US2.1                     | Flight Attendant | input a brief description of a conflict scenario into the chatbot | the chatbot can understand the intent of the situation                   | Must Have    | 1 story point   | Enables customized simulation entry to support a user input. Story Points: Making an initial Input window is easy, which can be replaced when the Formal UI is being made. Priority: This is compulsory, without this, nothing could be done|
| US2.2                     | User | Able to select my role in this simulation | The chatbot can simulate the scenario more accurately                   | Should Have    | 1 story point | Help chatbot to realize the role of the user. Story Points: Making a sidebar for selecting role and output to chatbot, which is easy and will be replaced when the Formal UI is made. Priority: This should have since it could help guide the chatbot in a clearer direction|
| US2.3                     | Flight Attendant | receive a matched scenario suggestion based on my input   | I can review past examples before starting simulation                   | Must Have    | 5 story points   | Supports case-based learning. Story Points: 5,  Make a RAG requires more effort. Priority: This is compulsory since the client wants this       |
| US2.4                     | Flight Attendant | choose to view a similar past case or skip to simulate | I can decide how much context I want before training                    | Could Have  | 2 story points   | Provides user flexibility. Story Points: 2. Maybe the current LLM can automatically do this after fine-tuning. Priority: This could be done to provide more user-friendly, but not our main target |
| US2.5                     | Flight Attendant | engage in a realistic conversation with a virtual passenger | I can practice conflict handling in a natural, multi-turn dialogue  | Must Have    | 10 story points   | Core function of role-play. Story Points: 10, this functionality needs to be fine-tuned on the LLM and tested. Priority: This is compulsory, and it is the core requirement from the client  |
| US2.6                     | Flight Attendant | experience varying passenger tone and emotional levels | I can train for a range of real-life behaviors                          | Should Have  | 2 story points   | Improves realism and training depth.Story Points: 2. Maybe the current LLM can automatically do this after fine-tuning. Priority: This could be done to provide more real experience, but not our main target |
| US2.7                     | Flight Attendant | restart the simulation using a different strategy      | I can explore alternate handling methods                                | Should Have   | 1 story points   | Provide repeat traning. Story Points: 1, the current LLM can automatically do this, or just restart. Priority: This should be done to provide more opportunity to the user |
| US2.8                    | Flight Attendant | be prompted with self-reflection questions             | I can think deeper about tone, behavior, and professionalism            | Could Have  | 5 story points   | Reinforces training retention. Story Points: 5, need to fine-tune the LLM to make it automatically do this after simulation. Priority: This could be done to reflect the core value of this project (training )    |
| US2.9                    | Flight Attendant | give feedback on realism and helpfulness of the simulation | chatbot can improve simulation quality                              | Could Have   | 2 story point    | Supports continuous improvement. Story Points: 2, the current LLM can change behavior based on user feedback or instruction, but needs to be tested in this case. Priority: This could be done to improve user experience|
| US2.10                    |User| have an app for me|  I can have a conversation with the chatbot | Must Have   | 1 story point    |Have an initial input method for the user. Story Points: 1, it can be done via terminal initially, which will be integrated into a UI in the next sprint. Priority: This must be done to enable input|

### User Goal: Practice handling passenger misconduct professionally

### Step 1: Scenario Input and role selection
  - US2.10 - Have a way to input(Must Have)
  - US2.2 - Select the role in simulation (Should Have)
  - US2.1 - Input conflict scenario description (Must Have) [Depends on US2.10]

### Step 2: Case Retrieval
  - US2.3 - Receive matched scenario cases from database (Must Have) [Depends on US2.1]
  - US2.4 - Choose to view case or skip (Could Have) [Depends on US2.2]

### Step 3: Simulation
  - US2.5 - Engage in realistic multi-turn conversation (Must Have) [Depends on US2.1, optionally US2.2]
  - US2.6 - Vary emotional tone of passenger (Should Have) [Depends on US2.4]
  - US2.7 - Restart simulation with new strategy (Should Have) [Depends on US2.4]

### Step 4: Reflection & Feedback
  - US2.8 - Prompted with self-reflection questions (Could Have) [Depends on US2.4]
  - US2.9 - Give feedback on realism (Could Have) [Depends on US2.4]

![image](https://github.com/user-attachments/assets/f90db0a8-2e9d-41ce-8fae-7876fa81294a)


### Burndown Chart
![image](https://github.com/user-attachments/assets/20def231-1c45-4427-8075-30e1ec287a06)
