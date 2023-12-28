import os
import logging
from deep_translator import GoogleTranslator
import google.generativeai as genai
import time


gemini_api_key = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-pro')


logging.basicConfig(filename='gemini_requests.log', level=logging.INFO)

while True:
    user_input = input("Enter your question (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break


    translated_input = GoogleTranslator(source='auto', target='en').translate(user_input)

    try:

        start_time = time.time()
        response = model.generate_content(translated_input)
        end_time = time.time()

        logging.info(f"Request: {translated_input}, Response: {response.text}, Time: {end_time - start_time}s")

        print("Response:\n" + response.text)
        feedback = input("Was this response helpful? (Yes/No): ")
        logging.info(f"Feedback: {feedback}")

    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"Error: {e}")
