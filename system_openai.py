import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

client = openai.OpenAI()



def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2
    )
    return response.choices[0].message.content

response = get_completion(f"""
iven the material topic: Reclaimed products and their packaging material, and the question: Can you provide information on how the data for reclaimed products and their packaging materials was collected, evaluate the provided user answer: We collect data for reclaimed products and their packaging materials through a rigorous process. We conduct regular audits of our supply chains or collaborate with third-party auditors. These audits specifically assess the sustainability and environmental impact of the products, with a particular focus on the use of reclaimed materials. The data collected from these audits is then carefully analyzed to ensure our products meet the highest environmental standards., according to the guidelines: , industry: Oil and gas. Provide a response in JSON format with the following fields:
1. 'rating': - a number between 1 and 3, where 1 means 'needs improvement', 2 means 'meets most criteria', and 3 means 'meets all specified criteria' as defined in the guidelines. The rating is specifically for the provided user answer based on guideline.
2. 'positive_reason_for_rating' - a brief positive explanation for the given rating. If no positive explanation, this field should be left blank.
3. 'negative_reason_for_rating' - a brief negative explanation for the given rating. If no negative explanation, this field should be left blank.
4. 'example_response': - if the rating is 2, Just refine the provided user answer, strictly ensuring it only aligns with the information provided in the user answer without adding any new values or making assumptions or halucinations. If the rating is 3, this field should be left blank. If the rating is 1, this field should be 'Unable to improve the content as it doesn't follow the guidelines.Please update the answer using the guidelines and try again.'.
""")
print(response)

