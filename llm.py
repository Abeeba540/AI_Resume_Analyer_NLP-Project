import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GROQ_API_KEY = os.getenv("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
")
GROQ_BASE_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {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
}",
    "Content-Type": "application/json"
}

def analyze_with_llm(resume_text, jd_text):
    prompt = f"""
You are an expert career advisor and hiring manager.
Evaluate the following resume against the given job description. Provide:
1. Fit Score (0 to 100).
2. Reasoning for the score.
3. Whether the candidate is a good fit (Yes/No).
4. Top strengths and key improvement areas.
5. A short hiring recommendation summary.

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are an expert in resume evaluation."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }

    # print("🔍 Debug: GROQ_API_KEY loaded:", bool(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
))
    # print("🔍 Debug: Headers being sent:", HEADERS)
    # print("🔍 Debug: Payload being sent:", payload)

    try:
        response = requests.post(GROQ_BASE_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()
        # print("✅ Success: Response received.")
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as http_err:
        # print("❌ HTTPError:", response.text)
        return f"⚠️ LLM evaluation failed: {http_err}"
    except Exception as e:
        # print("❌ General Exception:", str(e))
        return f"⚠️ LLM evaluation failed: {e}"
# analyze_with_llm("sghagdh","jgdhd")
