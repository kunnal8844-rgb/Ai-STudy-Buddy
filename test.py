import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("Gemeni_Api_key")
)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(
    "Explain Artificial Intelligence in one sentence."
)

print(response.text)