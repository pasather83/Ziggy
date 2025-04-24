from flask import Blueprint, request, jsonify
import json
from app.utils import find_answer
from flask_cors import CORS

app = Blueprint('ziggy', __name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask_ziggy():
    data = request.get_json()
    question = data.get('question', '').lower()

    with open('backend/knowledge_base.json', 'r') as f:
        knowledge_base = json.load(f)

    answer = find_answer(question, knowledge_base)
    return jsonify({ "answer": answer })
