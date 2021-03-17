from flask import Flask, request, jsonify
from datetime import datetime
import json, uuid

app = Flask(__name__)

@app.route('/', methods=['POST'])
def mail_json():
    content = request.get_json()
    name = datetime.now().strftime('%Y-%m-%d--%H:%M:%S') + '-' + uuid.uuid4().hex + '.json'
    with open(name, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)
    return content

