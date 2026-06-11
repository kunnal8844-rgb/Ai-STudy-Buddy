import google.generativeai as genai

genai.configure(
    api_key="AQ.Ab8RN6Iu2bnpGEsQ3DfDSKdLMIDL8ST-KlpDF6_48JHK33PjYg"
)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(
    "Explain Artificial Intelligence in one sentence."
)

print(response.text)