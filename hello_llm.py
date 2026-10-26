import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client() 

response = client.models.generate_content(
    model=os.getenv("MODEL"),
    contents="what is AI",
    

)

print(response.text)