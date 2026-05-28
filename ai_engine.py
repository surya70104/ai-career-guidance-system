import google.generativeai as genai

genai.configure(
    api_key="AIzaSyC3er1TzHp6OyInyNT7n3V1RJux7oKQhcs"
)

model = genai.GenerativeModel(
    "models/gemini-flash-lite-latest"
)

def ask_ai(prompt):

    response = model.generate_content(prompt)

    return response.text