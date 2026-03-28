import os
import json
from flask import Flask, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)
client = genai.Client()

@app.route('/classify', methods=['POST'])
def classify_environment():
    try:
        data = request.get_json()
        if not data or 'sensor_reading' not in data:
            return jsonify({"error": "Missing 'sensor_reading' in request body."}), 400
        
        sensor_text = data['sensor_reading']

        system_instruction = """
        You are an industrial safety AI agent. Analyze the following environment sensor data.
        Classify the situation strictly as "Normal", "Warning", or "Critical".
        Provide a one-sentence justification.
        """

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=sensor_text,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json",
                response_schema={
                    "type": "OBJECT",
                    "properties": {
                        "status": {"type": "STRING", "enum": ["Normal", "Warning", "Critical"]},
                        "justification": {"type": "STRING"}
                    },
                    "required": ["status", "justification"]
                }
            )
        )

        agent_result = json.loads(response.text)
        return jsonify(agent_result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)