# Backend Testing
This test is mainly to find potential logic errors in the backend workflow. The test is conducted on the Dify official website and uses the UI provided by Dify. No integration testing with our own frontend has been performed yet.
"Open" means there is a issue.
"Close" means there is no issue or the issue is resolved.

## Test result #1
Description: When selecting a tone, replying to something else will directly enter the simulation, and the tone seems to be randomly selected.

Status: Open
![image](https://github.com/user-attachments/assets/52ce8fd7-7e3e-43ea-a5b9-adc02a0dbf29)

Description: When confirming to start the simulation. If inputting yes or 1 such meaning "True" in programming, the simulation will start directly.

Status: Open
![image](https://github.com/user-attachments/assets/91fcd3c4-dd71-4bdf-8826-4293735cdd24)

Description: When entering "end", the conversation will end. This is correct.

Status: Close
![image](https://github.com/user-attachments/assets/28c855a8-f54c-4c5d-a32e-3d61e2e5871a)

Description: In some cases, when we need to select scenarios, if entering a word other than 1, 2, or 3, such as change or yes, it will not prompt you to remake a selection, and the first scenario will be selected directly.

Status: Open
![image](https://github.com/user-attachments/assets/151ab383-9b60-455f-acde-aac4410d0407)
![image](https://github.com/user-attachments/assets/44ad788f-0ab7-44d0-8a2d-a5917960e354)


