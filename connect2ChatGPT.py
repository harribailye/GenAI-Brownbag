# Import libaries 
from openai import OpenAI

# Set API key 
client = OpenAI(
    api_key="",
) 

# Define the System Role
messages = [ {"role": "system", "content": "Your responses should not exceed one sentence in length."} ]

# Text prompt 
user_prompt = input("Enter your question (or type 'exit' to quit): ")
messages.append({"role": "user", "content": user_prompt})

# Set up the model and send the user prompt
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages= messages
) 

# Print the model output 
print(response.choices[0].message)
