from groq import Groq
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
import json
from typing import Optional
from dotenv import load_dotenv
import os


app = FastAPI()

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)

class TranslationRequest(BaseModel):
    text: str 
    source_lang: Optional[str] = Field(
        "auto",
        description="Source language code or 'auto' for auto-detection",
        example="English",
    )
    target_lang: Optional[str] = Field("English", description="Target language for translation")



system_prompt = (""" You are **TransBot**, a fast, accurate multilingual translation agent.
   ### CORE TASK
    1. **Detect** the language of the input text automatically (never ask the user).
    2. **Translate** the text to the **target language** specified by the user.
    3. **Always respond with a JSON object** in this **exact format**:

    ```json
    {
    "source_lang": "<ISO-639-1 code>",
    "target_lang": "<ISO-639-1 code>",
    "translation": "<translated text>"
    }
    ###RULES
    - Use ISO-639-1 two-letter codes (e.g., en, es, fr, de, zh, ja, ar, hi, pt, ru, ko, etc.).
    - If the user writes a full language name (e.g., "Spanish"), map it to the correct code.
    - Preserve all formatting: line breaks, bullet points, code blocks, emojis, punctuation.
    - If source and target are the same → "translation" = original text.
    - If language detection fails → assume source is en.
    - Never add explanations, comments, or extra text outside the JSON.
    - Never escape or wrap the JSON — output raw valid JSON only.
                
""")


@app.post('/translate')
async def language_translator(req: TranslationRequest):
    text = req.text
    target_lang = req.target_lang
    if not target_lang:
        target_lang = "English"
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f""""Translate the following text to **{target_lang}**:\n\n\"\"\"\n{text}\n\"\"\""""
            }
        ]
    )
    response =  completion.choices[0].message.content
    return JSONResponse(
        content=json.loads(response),
        status_code= 200
    )


@app.get('/')
def hello():
    return "Welcome to home page"