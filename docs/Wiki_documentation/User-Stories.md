## User Story Overview
| ID  | As a...        | I want to...  | So that...       | Priority         |Size estimation|Status                           |
|-----|----------------|---------------|------------------|------------------|------------------|---------------------------------|
| US1 | Maintenance Technician (Michael Thompson)    | Engage in CRMSON-powered scenario dialogue simulating maintenance errors or missed CAT status updates    |I can reflect on my decision-making and procedural compliance in realistic, high-pressure situations|Should Have| Large| Draft|
| US2 | Flight Attendant (Olivia Carter)   |Practice handling difficult passenger behavior through CRMSON’s role-play simulations | I can strengthen my conflict de-escalation skills and ensure professional behavior under stress |Must Have | Large|In Progress|
| US3 | Commercial Airline Captain (James Walker)   | Simulate time-constrained decision-making around NOTOC discrepancies during pre-departure checks using CRMSON  |I can reflect on how I prioritize safety and communication in pressure-filled cockpit environments| Could Have |Large| Draft|
| US4 |Cabin Crew Lead (Noah Jensen)| Simulate an in-flight medical emergency conversation and resource coordination |I can assess my ability to lead calmly, communicate clearly, and adhere to protocol| Could Have |Medium| Draft|

## Detailed User Stories



### User Story ID: [US1]
* **Title:** Enhancing Maintenance Accuracy through Scenario Simulation  
* **As a** Maintenance Technician (Michael Thompson), **I want to**  Engage in CRMSON-powered scenario dialogue simulating maintenance errors or missed CAT status updates **so that**  I can reflect on my decision-making and procedural compliance in realistic, high-pressure situations.  
* **Priority:** Should Have  
* **Status:** Draft  
* **Estimation:** 5 story points / 1 week
* **Acceptance Criteria:**  
   - User can input a brief description of a maintenance issue or uncertainty.
   - System retrieves a relevant real-world case or simulation scenario. 
   - Multi-turn dialogue simulates realistic conversations around procedural steps, CAT status, or decision points. 
* **Dependencies:**
   - Requires access to a maintenance incident dataset.
   - Relies on embedding search for matching scenarios.
* **Notes:**
   - Security practices in place for access control.
   - User interactions are logged anonymously for audit & training data.

Product Backlog Considerations

* **Epic:** Maintenance Simulation Engine
* **Sprint Placement:** Sprint 2 after US2 or Sprint 3
* **Business Value:**
   - Helps technicians build procedural awareness through experiential learning.
   - Reduces likelihood of repeated errors by enabling reflective practice.
   - Supports SMS (Safety Management System) goals.




### User Story ID: [US2]
* **Title:** Handling Passenger Misconduct with Professionalism
* **As a** Flight Attendant (Olivia Carter), **I want to**  Practice handling difficult passenger behavior through CRMSON’s role-play simulations, **so that**  I can strengthen my conflict de-escalation skills and ensure professional behavior under stress.  
* **Priority:** Must have 
* **Status:** In Progress
* **Estimation:** 20 story points / 4 weeks
* **Acceptance Criteria:**  
   - User can input a brief scenario intent in natural language (e.g., “passenger won't sit down”).
   - System retrieves a relevant misconduct case or begins a direct LLM simulation.
   - Role-play supports multi-turn, emotionally dynamic conversations with branching behavior.
   - System provides a reflection summary with language, tone, and escalation indicators. 
* **Dependencies:**
   - Intent classification and embedding-based scenario matching
   - UI for input + chat-based simulation
   - Pre-defined tone profiles for LLM role-play variation
* **Notes:**
   - LLM responses must maintain realistic tone & emotional variation.
   - Interaction history anonymized for reflection and audit.

Product Backlog Considerations

* **Epic:** Inflight Conflict Simulation
* **Sprint Placement:** Sprint 2
* **Business Value:**
   - Enhances flight attendants’ ability to manage passenger conflict without escalation
   - Promotes consistency and professionalism under pressure
   - Reduces need for in-person role-play training, improving scalability of crew preparation




### User Story ID: [US3]
* **Title:** Resolving NOTOC-Closeout Conflicts Before Takeoff
* **As a** a Commercial Airline Captain(James Walker), **I want to**  Simulate time-constrained decision-making around NOTOC discrepancies during pre-departure checks using CRMSON, **so that**  I can reflect on how I prioritize safety and communication in pressure-filled cockpit environments.  

* **Priority:** Could Have 
* **Status:** Draft 
* **Estimation:** 10 story points / 2 weeks
* **Acceptance Criteria:**  
   - System accepts a brief flight prep situation input involving NOTOC or closeout confusion.
   - LLM simulation presents realistic time-critical communication with Ops, Dispatcher, or Crew Chief.
   - Simulation enables different paths (delay, proceed with conditions, escalate) and evaluates decision-making.
   - Reflective summary includes regulatory adherence, communication clarity, and time management. 
* **Dependencies:**
   - Case dataset including NOTOC or RA issues
   - Domain knowledge embedded in LLM prompts (e.g., RA rules, communications SOPs)
   - UI to input scenario and navigate role-play
* **Notes:**
   - Simulation tone should reflect cockpit urgency.
   - Must support multiple resolution paths for training flexibility.

Product Backlog Considerations

* **Epic:** Departure Compliance Simulation
* **Sprint Placement:** Sprint 3
* **Business Value:**
   - Builds captain confidence in high-pressure regulatory decision-making
   - Improves crew coordination around paperwork and pre-departure procedures
   - Reduces miscommunication and unnecessary delays




### User Story ID: [US4]
* **Title:** Simulating In-Flight Medical Emergency Coordination
* **As a** Cabin Crew Lead (Noah Jensen), **I want to**  simulate an in-flight medical emergency conversation and coordinate resources using CRMSON, **so that**  I can assess my ability to lead calmly, communicate clearly, and adhere to protocol.

* **Priority:** Could Have 
* **Status:** Draft 
* **Estimation:** 3 story points / 1 week
* **Acceptance Criteria:**  
   - User can initiate a simulation by describing a medical emergency scenario (e.g., unconscious passenger in row 14).
   - LLM simulates dialogue with passengers, other cabin crew, and possibly the pilot or MedLink.
   - System supports decision branching (e.g., request for defibrillator, page doctor, notify cockpit).
   - Reflective summary is generated, highlighting leadership, clarity, protocol adherence, and emotional tone.
* **Dependencies:**
   - Medical protocol knowledge embedded in prompt templates
   - UI support for real-time decision tree or open text input
   - Pre-tagged conversation paths for varied emergency outcomes
* **Notes:**
   - Simulation should escalate naturally and adapt to user input
   - Option to simulate coordination with cockpit and external medical assistance

Product Backlog Considerations

* **Epic:** Emergency Preparedness Simulation
* **Sprint Placement:** Sprint 3
* **Business Value:**
   - Helps senior cabin crew build leadership confidence in high-stress medical situations
   - Enhances communication and decision-making consistency in emergency scenarios
   - Supports regulatory and airline training requirements on medical emergencies

