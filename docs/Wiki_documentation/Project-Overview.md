# Project Overview

## Project Name: [Involo Agent Builder]
## Team Members:
- Xiang Zhou (xianzhou2@student.unimelb.edu.au)
- Hongkun Zhang (hongkunz@student.unimelb.edu.au)
- Yifeng Su (yifengs@student.unimelb.edu.au)
- Junbo Liang (junbol@student.unimelb.edu.au)
- Yutao Zhou (yutazhou@student.unimelb.edu.au)

## Team Roles and Responsibility:
| Name         | Role           | Responsibility      |
|--------------|--------------|--------------------|
| Junbo Liang  |Product Owner| Responsible for product vision, demand prioritization, and communication with customers/teams |
| Xiang Zhou   |Scrum Master|Promote agile processes, Help the team solve obstacles ,Ensure efficient team collaboration, Prevent technical debt accumulation, Ensure the quality of final delivery (test AI results to ensure compliance with offline operation requirements)|
| Yifeng Su    | Developer    |vector database construction, Processing aviation manuals and accident data|
| Hongkun Zhang| Developer    |Large language model deployment, fine-tuning optimization |
| Yutao Zhou   | Developer    |Large language model deployment,  inference optimization |

## Project Goal
The goal of this project is to develop **CRMSON**, a multi-agent AI chatbot designed to enhance team resilience in high-stakes environments such as aviation. By leveraging a proprietary dataset of team dynamics and aviation incidents, CRMSON provides evidence-based recommendations to improve communication, mitigate authority gradients, and address sociocultural challenges like sexism and racism.  

The system enables users to:  
- Generate tailored conversational strategies  
- Simulate interactions to prevent escalation  
- Reference relevant regulations to foster more effective teamwork  

Currently, we aim to build an **agent builder** capable of:  
- Generating AI agents based on aviation incident reports  
- Analyzing and comparing regulatory guidelines  
- Enhancing decision-making and conflict resolution  

## Technologies Used
- GitHub
- Python/JavaScript/etc.
- Other tools

## Scope
### In-Scope and Out-of-Scope
  - Only reports of aircraft carrying **passengers** are considered. Other mission types such as **training** and **cargo**, are not included in the training and testing process of this project.
  - Only reports of **communication breakdowns** between people are considered. Other reasons such as **maintenance** and **technical** issues are not included in the training and testing process of this project.
  - Only includes the core functionality for AI chatbots regarding **flight safety**, and other high-risk environment communications such as **submarines** and **nuclear power plants** are not included in this project.
  - Only includes the **typical** safety flight scenarios shown in the dataset, such as approach control and missed approach procedures, and **new scenarios** not present in the dataset will not be included.
  - Only uses the flying dictionary to **fine-tune** of existing open-source LLMs, **research and development** of advanced natural language processing algorithms is not included.
  - Only uses **open-source LLMs** and **proxy platforms**, **dedicated servers** and **paid LLMs** are not included.
  - Only considers generating the scenarios in **English**, the precise and  accurate translation of terms into **other languages** are not included.
  - Only produces the **individual** AI chatbots, the **integration** with Border’s internal systems, such as dispatch system and flight log system are not included.

### Functional requirements
  - Understand the scenarios prompted by the user, analyze and provide the top k relevant existing scenarios to the user.
  - Search for external resources and provide some reference rules.
  - Generate scenarios and chat with users for training purposes.
  - UI design suitable for user interaction.

### Non-Functional requirements
  - It does not have dependencies on the platform and LLM currently used. Can be adapted to a dedicated server and using paid LLM once we have resources.
  - Users' privacy should be protected.
  - Most of the time, the system should be available.
  - Once we have enough resources, can upgrade the system to generate more scenarios. It should have good scalability.
  - Reasonable response time, should not crash at high throughput.

## Timeline
- **Sprint 1:** Inception(Research & Planning) (14/03/2025 - 04/04/2025)
- **Sprint 2:** Development (04/04/2025 - 02/05/2025)
- **Sprint 3:** Testing & Deployment (02/05/2025 - 30/05/2025)
- **Sprint 4:** Product Handover (30/05/2025 - 13/06/2025)
