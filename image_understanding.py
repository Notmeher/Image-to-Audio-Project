import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


GOOGLE_API_KEY = os.getenv("API_KEY_GEN")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')

def get_response(image):
    query = "Describe the image in one sentence."
    response = model.generate_content([query, image], stream=True)
    response.resolve()
    return response.text

