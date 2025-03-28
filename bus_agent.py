import requests
import os

import requests
#this gets the cards from the Trello board
# Trello API endpoint and credentials
list_id = "5f1743793b184e31ee7d27fb"  # this is the id of the to do list.
api_key = "d200138058c063cbb4ccd1c46bb572a0"  # Replace with your Trello API key
api_token = "ATTA2e7844b7cbb2557cf79ef8cd019d9f64f0fc77840bc4410149219a6f447c56b4D33239C4"  # Replace with your Trello API token

# Trello API URL to get cards in a list
url = f"https://api.trello.com/1/lists/{list_id}/cards"

# Query parameters
params = {
    "key": api_key,
    "token": api_token,
    "fields": "name,desc"  # Only fetch the name and description fields
}

# Make the API request
response = requests.get(url, params=params)

# Check the response
if response.status_code == 200:
    cards = response.json()  # Parse the JSON response
    for card in cards:
        print(f"Card Name: {card['name']}")
        print(f"Card Description: {card['desc']}")
        print("-" * 40)  # Separator for readability
else:
    print("Failed to fetch cards. Status code:", response.status_code)
    print("Response:", response.text)
    
# Define the URL and headers for IBM IAM token request
url = 'https://iam.cloud.ibm.com/identity/token'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Define the payload (data) for the POST request
data = {
    'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
    'apikey': 'GTH2VlKdyck3k1lBELX6VRYb2Qo-_dA2ocSgOzWhRvAo'
}

# Make the POST request to get the access token
response = requests.post(url, headers=headers, data=data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response to get the access token
    access_token = response.json().get('access_token')
    print("Access Token:", access_token)
else:
    print("Failed to retrieve access token. Status code:", response.status_code)
    print("Response:", response.text)
    exit(1)  # Exit if the token request fails


# Set environment variables
os.environ["WATSONX_ACCESS_TOKEN"] = access_token
os.environ["SERPER_API_KEY"] = "82c11076c852aaa5029574c2e2e8f00e55a1e9aa"

# Watsonx API configuration
WATSONX_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
WATSONX_PROJECT_ID = "86aad677-bf5f-4626-af40-97091e73a467"
WATSONX_MODEL_ID = "ibm/granite-3-8b-instruct"

# Parameters for text generation
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 500,
    "min_new_tokens": 50,
    "repetition_penalty": 1
}

# Function to call Watsonx API
def watsonx_text_generation(prompt, access_token, project_id, model_id, parameters):
    url = WATSONX_URL
    
    body = {
        "input": prompt,
        "parameters": parameters,
        "model_id": model_id,
        "project_id": project_id,
        "moderations": {
            "hap": {
                "input": {
                    "enabled": True,
                    "threshold": 0.5,
                    "mask": {
                        "remove_entity_value": True
                    }
                },
                "output": {
                    "enabled": True,
                    "threshold": 0.5,
                    "mask": {
                        "remove_entity_value": True
                    }
                }
            },
            "pii": {
                "input": {
                    "enabled": True,
                    "threshold": 0.5,
                    "mask": {
                        "remove_entity_value": True
                    }
                },
                "output": {
                    "enabled": True,
                    "threshold": 0.5,
                    "mask": {
                        "remove_entity_value": True
                    }
                }
            }
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"  # Use the access token here
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code != 200:
        raise Exception(f"Non-200 response: {response.status_code} - {response.text}")

    data = response.json()

    # Ensure the response structure is as expected
    if 'results' in data and len(data['results']) > 0 and 'generated_text' in data['results'][0]:
        return data['results'][0]['generated_text']
    else:
        raise Exception("Unexpected response structure: " + str(data))

# Function to perform a web search using Serper API
def serper_search(query, api_key):
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "q": query
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"Serper API error: {response.text}")
    return response.json()

# Custom Agent class to replace crewai Agent
class CustomAgent:
    def __init__(self, access_token, project_id, model_id, parameters, role, goal, backstory, tools, verbose=False):
        self.access_token = access_token
        self.project_id = project_id
        self.model_id = model_id
        self.parameters = parameters
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.tools = tools
        self.verbose = verbose

    def execute_task(self, task_description):
        if self.verbose:
            print(f"🤖 {self.role} is working on: {task_description}")
        
        # Use the Watsonx API to generate a response
        response = watsonx_text_generation(task_description, self.access_token, self.project_id, self.model_id, self.parameters)
        
        if self.verbose:
            print(f"📝 Response: {response}")
        
        return response

# Custom Task class to replace crewai Task
class CustomTask:
    def __init__(self, description, expected_output, output_file, agent):
        self.description = description
        self.expected_output = expected_output
        self.output_file = output_file
        self.agent = agent

    def execute(self):
        result = self.agent.execute_task(self.description)
        
        # Save the result to a file
        with open(self.output_file, "w") as f:
            f.write(result)
        
        return result

# Initialize the custom LLM
access_token = os.environ["WATSONX_ACCESS_TOKEN"]

# Create the researcher agent
researcher = CustomAgent(
    access_token=access_token,
    project_id=WATSONX_PROJECT_ID,
    model_id=WATSONX_MODEL_ID,
    parameters=parameters,
    role="Senior AI Researcher",
    goal=card['desc'],   #f"Find promising research in the field of quantum computing.{card['desc']}",
    backstory="You are a veteran quantum computing researcher with a background in modern physics.",
    tools=[serper_search],
    verbose=True
)

# Create the writer agent
writer = CustomAgent(
    access_token=access_token,
    project_id=WATSONX_PROJECT_ID,
    model_id=WATSONX_MODEL_ID,
    parameters=parameters,
    role="Senior Speech Writer",
    goal="Write engaging and witty keynote speeches from provided research.",
    backstory="You are a veteran quantum computing writer with a background in modern physics.",
    tools=[],
    verbose=True
)

# Create the Leadership agent
leader = CustomAgent(
    access_token=access_token,
    project_id=WATSONX_PROJECT_ID,
    model_id=WATSONX_MODEL_ID,
    parameters=parameters,
    role="Senior Vice President and Director, IBM Research",
    goal="Come up with a step by step plan to implement the research into a product at IBM. Create a vision and a roadmap for the company.",
    backstory="You are a veteran quantum computing writer with a background in modern physics.",
    tools=[],
    verbose=True
)

# Create the tasks
task1 = CustomTask(
    description="Search the internet and find 5 examples of promising AI research.",
    expected_output="A detailed bullet point summary on each of the topics. Each bullet point should cover the topic, background and why the innovation is useful.",
    output_file="task1output.txt",
    agent=researcher
)

task2 = CustomTask(
    description="Write an engaging keynote speech on quantum computing.",
    expected_output="A detailed keynote speech with an intro, body and conclusion.",
    output_file="task2output.txt",
    agent=writer
)

task3 = CustomTask(
    description="Write a detailed plan to implement the ai and quantum computing research into a product at IBM. Create a vision and a roadmap for the company.",
    expected_output="A detailed plan that includes a vision and a roadmap for IBM.",
    output_file="task3output.txt",
    agent=leader
)

# Execute the tasks
print("🚀 Starting task 1...")
task1_result = task1.execute()
print("✅ Task 1 completed. Output saved to task1output.txt")

print("🚀 Starting task 2...")
task2_result = task2.execute()
print("✅ Task 2 completed. Output saved to task2output.txt")

print("🚀 Starting task 3...")
task3_result = task3.execute()
print("✅ Task 3 completed. Output saved to task3output.txt")