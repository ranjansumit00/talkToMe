from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"  # Ollama local server

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = f"""
You are a helpful AI assistant. The user will ask general questions. Respond clearly and informatively within 150 words.

User: {data.get('prompt')}
AI:
"""

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    payload = {
        "model": "gemma3",  # or "gemma:3b", "mistral", etc.
        "prompt": prompt,
        "stream": False
    }
    

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return jsonify({"response": result.get("response", "")})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,port=5000)
