import delimited
import openai
from openai import OpenAI

api_key = "sk-ycneMaMqkMDhKnf3BlQbbJMIhcz790kU3SXd1TMClCT3BlbkFJWJAji9SAdnCZZz5dddhlbJ5bznkfeubhaQXmagXfAA"

client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
)
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response_open_ai = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness o
    )
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


