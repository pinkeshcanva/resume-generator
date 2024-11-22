from flask import Flask, request, jsonify
import openai
import asyncio
from aiohttp import ClientSession

app = Flask(__name__)

# OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Create async request handling
async def get_openai_response(prompt):
    async with ClientSession() as session:
        response = await session.post(
            "https://api.openai.com/v1/completions",
            headers={
                "Authorization": f"Bearer {openai.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "text-davinci-003",
                "prompt": prompt,
                "max_tokens": 500
            },
        )
        response_json = await response.json()
        return response_json

@app.route('/generate', methods=['POST'])
async def generate():
    data = request.json
    job_title = data.get('job_title')
    experience = data.get('experience')
    company_info = data.get('company_info')
    template_type = data.get('template_type')

    # Constructing a prompt based on the template type
    if template_type == "resume":
        prompt = f"Create a detailed resume for a {job_title} using the following experience:\n{experience}\n with additional company context:\n{company_info}"
    else:
        prompt = f"Write a cover letter for a {job_title} job based on this experience:\n{experience}\n and company information:\n{company_info}"

    # Call OpenAI API asynchronously
    response_json = await get_openai_response(prompt)
    generated_text = response_json['choices'][0]['text'].strip()

    return jsonify({"generated_text": generated_text})

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
