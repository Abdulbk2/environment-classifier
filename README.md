# Environment Status Classifier (ADK + Gemini)

This project is a submission for Track 1: Build and deploy AI agents using Gemini, ADK, and Cloud Run. 

It is a serverless AI agent that processes raw environmental sensor payloads and classifies the environment's safety status using the Agent Development Kit (ADK) and the Gemini model.

## Live Endpoint
**Cloud Run URL:** `https://environment-classifier-965740091063.asia-southeast1.run.app/classify`

## Problem Statement & Capability
The agent performs one clearly defined task: **Text Classification of Sensor Data**. 

It accepts a JSON payload containing raw text from simulated field sensors (e.g., temperature, humidity, smoke detection) and outputs a strict JSON response categorizing the environment as `Normal`, `Warning`, or `Critical`, along with a generated justification.

## Technologies Used
* **Framework:** Flask (Python)
* **AI/Agent:** Google GenAI SDK (ADK) / Gemini 2.5 Flash
* **Deployment:** Google Cloud Run, Docker, Gunicorn

## How to Test the Agent
You can test the live Cloud Run endpoint using the following cURL command:

```bash
curl -X POST https://environment-classifier-965740091063.asia-southeast1.run.app/classify /
-H "Content-Type: application/json" \
-d '{"sensor_reading": "Temperature 45C, pressure dropping rapidly, faint smoke detected."}'
