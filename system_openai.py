import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

client = openai.OpenAI()



def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2
    )
    return response.choices[0].message.content

# response = get_completion(f"""
# iven the material topic: Reclaimed products and their packaging material, and the question: Can you provide information on how the data for reclaimed products and their packaging materials was collected, evaluate the provided user answer: We collect data for reclaimed products and their packaging materials through a rigorous process. We conduct regular audits of our supply chains or collaborate with third-party auditors. These audits specifically assess the sustainability and environmental impact of the products, with a particular focus on the use of reclaimed materials. The data collected from these audits is then carefully analyzed to ensure our products meet the highest environmental standards., according to the guidelines: , industry: Oil and gas. Provide a response in JSON format with the following fields:
# 1. 'rating': - a number between 1 and 3, where 1 means 'needs improvement', 2 means 'meets most criteria', and 3 means 'meets all specified criteria' as defined in the guidelines. The rating is specifically for the provided user answer based on guideline.
# 2. 'positive_reason_for_rating' - a brief positive explanation for the given rating. If no positive explanation, this field should be left blank.
# 3. 'negative_reason_for_rating' - a brief negative explanation for the given rating. If no negative explanation, this field should be left blank.
# 4. 'example_response': - if the rating is 2, Just refine the provided user answer, strictly ensuring it only aligns with the information provided in the user answer without adding any new values or making assumptions or halucinations. If the rating is 3, this field should be left blank. If the rating is 1, this field should be 'Unable to improve the content as it doesn't follow the guidelines.Please update the answer using the guidelines and try again.'.
# """)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "text": "\"You are an expert assistant specializing in ESRS (European Sustainability Reporting Standards) and XBRL (eXtensible Business Reporting Language). Your role is to guide users in crafting accurate, compliant, and effective responses to disclosure requirements, ensuring alignment with ESRS and XBRL guidelines.\n\n### Key Objectives\n1. Provide expert guidance to understand and implement ESRS and XBRL standards effectively.\n2. Help users draft responses that meet disclosure requirements and standards.\n3. Evaluate user responses critically to identify strengths and areas for improvement.\n4. Refine user responses for correct spelling, grammar, and clarity.\n5. Format feedback in a structured JSON format to assist UI integration.\n\n---\n\n### Operational Guidelines\n1. **Understanding the User's Response:**\n   - If no response is provided or the response is incomplete, generate a detailed help text (max 500 words) to assist the user in starting to draft an effective answer.\n   - If the response is partially or fully provided:\n     - Evaluate its strengths based on the disclosure requirements.\n     - Identify gaps, missing elements, or invalid aspects as per the stated requirements.\n     - Refine the response for grammar, spelling, and clarity.\n     - Offer clear, actionable advice for improvement.\n\n2. **Contextual Focus:**  \nFor Disclosure Requirement **E2-2 – Actions and Resources Related to Pollution**, ensure the response addresses:\n   - **Point 16:** Disclosure of pollution-related actions and the resources allocated to their implementation.\n   - **Point 17:** Explanation of key actions taken and planned to achieve pollution-related policy objectives and targets.\n   - **Point 18:** Description of action plans and resources, as prescribed in ESRS 2 MDR-A, related to material sustainability matters.\n   - **Point 19:** Alignment of actions and resources with the mitigation hierarchy:\n     - (a) Avoid pollution (e.g., phase-out of harmful materials).\n     - (b) Reduce pollution (e.g., meeting Best Available Techniques or DNSH criteria under the EU Taxonomy Regulation).\n     - (c) Restore or regenerate ecosystems impacted by pollution.\n\n3. **Evaluation Priorities:**\n   - Does the response clearly outline actions and resources related to pollution management?\n   - Is the mitigation hierarchy (avoid, reduce, restore) appropriately addressed?\n   - Does the response align with ESRS 2 MDR-A and the EU Taxonomy Regulation’s DNSH criteria?\n   - Is the language precise, actionable, and compliant with ESRS disclosure standards?\n\n4. **Feedback Format:**  \nProvide feedback in the following JSON structure:\n```json\n{\n  \"help text\": \"Provide help text if the user's response is empty or incomplete.\",\n  \"what is good\": \"Highlight aspects of the response that comply with the requirements.\",\n  \"what could be improved\": \"Outline specific gaps, inaccuracies, or missing information that need to be addressed.\",\n  \"is response OK / needs further improvement\": \"Flag the response as 'OK' or 'NOT_OK' based on its compliance with the disclosure requirements.\"\n}\n```\n---\n\n### Purpose of This Prompt\n- Enable users to draft or refine responses to meet the specific requirements of **E2-2 – Actions and Resources Related to Pollution**.\n- Ensure responses are aligned with regulatory and reporting frameworks for sustainability and pollution mitigation.",
          "type": "text"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "Question Asked : \"\"How does your organization address pollution-related issues in alignment with Disclosure Requirement E2-2, including the key actions taken or planned, the resources allocated for their implementation, and the alignment of these actions with the mitigation hierarchy (avoid, reduce, and restore/regenerate ecosystems) as outlined in ESRS 2 MDR-A and EU Taxonomy Regulations?\"\"",
          "type": "text"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "text": "Our company is committed to addressing pollution-related issues as part of our sustainability strategy. We have implemented various measures to minimize our environmental impact and are allocating resources to further these efforts. We are aligning our actions with regulatory requirements and industry best practices, focusing on reducing pollution in our operations. Our efforts also include exploring ways to restore affected ecosystems where applicable. These initiatives reflect our commitment to sustainability in the context of battery production in Germany.",
          "type": "text"
        }
      ]
    }
  ]
)
print(response)

