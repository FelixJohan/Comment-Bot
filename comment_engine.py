import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_comment(context):
    prompt = f"Write a short, fun, and positive Instagram comment for this post:\n\n\"{context}\"\n\nComment:"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=60,
            temperature=0.8
        )
        
        comment = response['choices'][0]['message']['content'].strip()
        return comment
    
    except Exception as e:
        return f"Error: {str(e)}"
