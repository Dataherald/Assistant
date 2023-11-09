import requests
import json

HOST = "http://streamlit_engine.dataherald.ai/api/v1/questions"
DATABASES_IDS = {
    'RealEstate': '6537c3dc4cec532eccb7d6cc',
    'SenateStock': '65424c694cec532eccb7d766',
}

def answer_question(
        question: str,
        db_name: enumerate(DATABASES_IDS.keys()) = 'RealEstate'
) -> str:
    payload = {
        "db_connection_id": DATABASES_IDS[db_name],
        "question": question,
    }
    json_data = json.dumps(payload)
    response = requests.post(HOST, data=json_data)  
    if response.status_code == 201:
        return response.json()['response']
    else:
        return "Sorry, I don't know the answer to that question."
