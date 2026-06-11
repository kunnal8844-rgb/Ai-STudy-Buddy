import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request
import google.generativeai as genai

# Put your Gemini API Key here
genai.configure(
    api_key=os.getenv("Gemeni_Api_Key")
)
model = genai.GenerativeModel("gemini-2.5-flash")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":
        question = request.form["question"]

        try:
            response = model.generate_content(
                f"Explain this topic in simple student-friendly language:\n{question}"
            )
            answer = response.text

        except Exception as e:
            answer = f"Error: {e}"

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)