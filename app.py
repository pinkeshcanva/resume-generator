from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API key
openai.api_key = "YOUR_API_KEY"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    job_title = data.get('job_title')
    experience = data.get('experience')
    company_info = data.get('company_info')
    template_type = data.get('template_type')

    prompt = f"Generate a {template_type} for a job titled '{job_title}' based on the following experience:\n{experience}\n and company info:\n{company_info}."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
    )

    return jsonify({"generated_text": response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
