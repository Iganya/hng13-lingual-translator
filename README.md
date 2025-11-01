# TransBot API - Fast & Accurate Multilingual Translation Service

A lightweight **FastAPI**-based translation service powered by **Groq** and **Llama 3.3 70B**, designed for real-time, accurate, and format-preserving language translation.

---

## Features

- **Auto Language Detection** – No need to specify source language.
- **ISO-639-1 Standard Codes** – Full support for `en`, `es`, `fr`, `zh`, `ja`, `ar`, `hi`, `pt`, `ru`, `ko`, etc.
- **Preserves Formatting** – Line breaks, bullet points, code blocks, emojis, and punctuation are kept intact.
- **JSON-Only Output** – Clean, predictable responses with no extra text.
- **Same-Language Handling** – Returns original text if source = target.
- **Fallback Logic** – Defaults to English if detection fails.

---

## API Endpoint

### `POST /translate`

Translates input text to the specified target language.

#### Request Body (JSON)

```json
{
  "text": "Your text to translate here",
  "source_lang": "auto",           // Optional: default "auto"
  "target_lang": "Spanish"         // Optional: default "English"
}
```
#### Response(JSON)

```json
   {
   "source_lang": "en",
   "target_lang": "es",
   "translation": "Tu texto traducido aquí"
   }
```

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone hhttps://github.com/iganya/hng13-task-0.git
   cd your-repo
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up .env file 
   ```GROQ_API_KEY=your_groq_api_key_here```
   Get your API key from https://console.groq.com
5. Run the FastAPI application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
6. Access the API at `http://127.0.0.1:8000/`

