import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def build_ai_prompt(location, income, lifestyle, inflation_percent, adjusted_costs):
    items = "\n".join([f"- {k}: ₦{v:,}" for k, v in adjusted_costs.items()])
    return f"""
A Nigerian user in {location}, earning ₦{income:,}/month, lives a {lifestyle} lifestyle.
Due to {inflation_percent}% inflation, their adjusted costs are:
{items}
Suggest 2–3 culturally relevant ways to save money without reducing their lifestyle quality.
"""

def get_ai_suggestions(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
        return "You're overspending 🚨"