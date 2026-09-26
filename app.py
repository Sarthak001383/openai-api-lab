from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

user_prompt = input("Enter your AI prompt: ")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=user_prompt
)

print("\nAI Response:")
print(response.text)
