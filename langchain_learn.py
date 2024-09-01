import warnings
warnings.filterwarnings('ignore')
import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']
llm_model = "gpt-3.5-turbo"

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def get_completion(prompt, model=llm_model):
    client = openai.OpenAI()
    messages = [{"role": "user", "content": prompt}]
    response_open_ai = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness o
    )
    return response_open_ai.choices[0].message.content



# print(get_completion("What is 1+1?"))

# customer_email = """
# Arrr, I be fuming that me blender lid \
# flew off and splattered me kitchen walls \
# with smoothie! And to make matters worse,\
# the warranty don't cover the cost of \
# cleaning up me kitchen. I need yer help \
# right now, matey!
# """
# style = """American English \
# in a calm and respectful tone
# """

# prompt = f"""Translate the text \
# that is delimited by triple backticks 
# into a style that is {style}.
# text: ```{customer_email}```
# """

# print(prompt)
# response = get_completion(prompt)
# print(response)

chat = ChatOpenAI(temperature=0.0, model=llm_model)
template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""
prompt_template = ChatPromptTemplate.from_template(template_string)
print(prompt_template)
print(prompt_template.messages[0].prompt)
print(prompt_template.messages[0].prompt.input_variables)

customer_style = """American English \
in a angry tone
"""
customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""
customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_email)

print(type(customer_messages))
print(type(customer_messages[0]))
print(customer_messages[0])

customer_response = chat(customer_messages)
print(customer_response.content)

service_reply = """Hey there customer, \
the warranty does not cover \
cleaning expenses for your kitchen \
because it's your fault that \
you misused your blender \
by forgetting to put the lid on before \
starting the blender. \
Tough luck! See ya!
"""
service_style_pirate = """\
a polite tone \
that speaks in English polite\
"""

service_messages = prompt_template.format_messages(
    style=service_style_pirate,
    text=service_reply)

print(service_messages[0].content)

service_response = chat(service_messages)
print(service_response.content)
