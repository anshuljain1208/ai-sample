import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file
api_key = "sk-ycneMaMqkMDhKnf3BlQbbJMIhcz790kU3SXd1TMClCT3BlbkFJWJAji9SAdnCZZz5dddhlbJ5bznkfeubhaQXmagXfAA"


client = openai.OpenAI(api_key=api_key)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

response = get_completion(f"""Take the letters in lollipop \
and reverse them""")
print(response)