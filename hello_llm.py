import os
from dotenv import load_dotenv
from google import genai

# 1. Load the key from .env into environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("GEMINI_API_KEY not found. Check your .env file.")

# 2. Create a client and send one prompt
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain what a token is in an LLM, in two sentences.",
)

# 3. Print the reply
print("Reply:\n", response.text)

# 4. Print the token usage the API returned
usage = response.usage_metadata
print("\nInput tokens: ", usage.prompt_token_count)
print("Output tokens:", usage.candidates_token_count)
print("Total tokens: ", usage.total_token_count)