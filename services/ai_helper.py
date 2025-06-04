import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

MAX_PROMPT_LENGTH = 4000

def load_prompt(file_path, **kwargs):
    with open(file_path) as f:
        return f.read().format(**kwargs)[:MAX_PROMPT_LENGTH]

def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini API Error: {str(e)}"
