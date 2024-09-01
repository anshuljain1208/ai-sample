import delimited
import openai
import os
from openai import OpenAI

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

client = OpenAI()
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response_open_ai = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness o
    ),
    return response_open_ai.choices[0].message.content

#Tactic 1
# text = f"""
# You should express what you want a model to do by \
# providing instructions that are as clear and \
# specific as you can possibly make them. \
# This will guide the model towards the desired output, \
# and reduce the chances of receiving irrelevant \
# or incorrect responses. Don't confuse writing a \
# clear prompt with writing a short prompt. \
# In many cases, longer prompts provide more clarity \
# and context for the model, which can lead to \
# more detailed and relevant outputs.
# """
#
# prompt = f"""
# Summarize the text delimited by triple backticks \
# into a single sentence.
# ```{text}```
# """

#Tactic 2

# prompt = f"""
# Generate a list of three made-up book titles along \
# with their authors and genres.
# Provide them in JSON format with the following keys:
# book_id, title, author, genre.
# """
prompt = f"""
Translate the following English text to Hindi: \
```Hi, I would like to order a blender```
"""
response = get_completion(prompt)
print(response)


