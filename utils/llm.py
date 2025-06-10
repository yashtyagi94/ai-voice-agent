# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# genai.configure(api_key=api_key)

# model = genai.GenerativeModel('gemini-pro')

# def generate_response(prompt):
#     response = model.generate_content(prompt)
#     return response.text

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Use a supported model
model = genai.GenerativeModel('models/gemini-1.5-flash')

def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text




