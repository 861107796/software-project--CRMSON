# How to Run the Dify on MRC
This guildline is mainly for the Windows user.

## 0. Unimelb VPN (Optional)

To connect the VM on MRC, you might need to connect to the unimelb VPN for the sack cyber security.
https://studentit.unimelb.edu.au/vpn
Download and install "GlobalProtect"

## 1. Connect to VM and Port forwarding
Make sure you have sent your key pair to the cloud manager, and you are using the corresponding privary key to connect.

### Method1: Using MobaXTerm
https://docs.cloud.unimelb.edu.au/guides/ssh_client/
Download and install it.
1. Connect to the VM first.
![alt text](image-4.png)
1. Click the Tunneling icon on the UI. ![alt ext](image.png)
2. Set up the Local port forwarding. ![alt text](image-1.png)
3. Select your privary key and run the tunneling. ![alt text](image-2.png)
4. Open http://localhost:8080 on your browser.

### Method2: Using Powershell
```shell
# Try to port forwarding
ssh -i <Your_Privary_key> -L 8080:localhost:80 ubuntu@115.146.92.189

# If does not work, need to check the permissions of your key
icacls <Your_Privary_key>
# Make sure there is only one left, such as BOB\Bob:(R)
# Ask GPT for how to remove the extra permissions
```
Open http://localhost:8080 on your browser.

## 2. Successfully Connected
For whom is connecting to the system for the first time, you may need to enter your username and password to log into the administrator account. The account information can be found in the root directory of the virtual machine, named "account.txt".
![alt text](image-5.png)
![alt text](image-3.png)


# How to Install Dify and Implement Workflow

This section is supplemental for situations where you might need to migrate your system to another cloud environment.

## 1. Dify installation

Follow official guidance:
https://docs.dify.ai/en/getting-started/install-self-hosted/docker-compose

## 2. Workflow implementation:

After logging in to the system, on the main page (http://localhost:8080/apps), follow the steps below to import the system's .yml file.
![alt text](image-6.png)

## 3. Model selection:

On the plugins page (http://localhost:8080/plugins), install the following model providers from Marketplace as listed below.
| Model | Usage | Necessity |
|-----|-----|-----|
|TONGYI|Input understanding and generate dialogue|compulsory|
|GroqCloud|Supplemental model provider|optional|
|SiliconFlow|Embedding model for knowledge base|compulsory|
|Hugging Face Hub|Supplemental model provider|optional|

![alt text](image-7.png)
Enter the API key of the model provider, you can follow the steps below.
1. Select the block that is using LLM model.
2. Select the model.
3. Click the "Model Provider Setting".
4. Click the "API KEY Setup" to setup the API Key you obtained from the API provider.
![alt text](image-8.png)
![alt text](image-9.png)

## 4. Knowledge base Setup

On the knowledge page (http://localhost:8080/datasets), create the knowledge base for situation retrieval.
1. Select the Knowledges tab.
2. Click the Create Knowledge.
![alt text](image-10.png)
3. Upload the dataset, for example the role_split_clean.csv from our github repository(IN-BlueRing/docs/role_split_clean.csv). 
![alt text](image-11.png)
4. Change the chuck length to 4000 (maximum).
5. Select your embedding model from the model provider.
![alt text](image-12.png)
6. Select the Hybrid Search and process.
![alt text](image-13.png)
7. Click the notification for checklist.
8. Click the "KNOWLEDGE"
9. Select the generated knowledge and click "Add".
![alt text](image-14.png)

