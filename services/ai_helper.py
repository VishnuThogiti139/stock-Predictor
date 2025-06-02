import google.generativeai as genai
import config

genai.configure(api_key=config.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

def load_prompt(file_path, **kwargs):
    with open(file_path) as f:
        return f.read().format(**kwargs)

def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini API Error: {str(e)}"