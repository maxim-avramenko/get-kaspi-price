from flask import Flask, request, jsonify
import subprocess
import json
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    data = request.get_json()

    try:
        result = subprocess.run(['python', "app.py", data["url"]], check=True, capture_output=True, text=True)
        res = json.loads(result.stdout)
        return jsonify(res), 200
    except subprocess.CalledProcessError as e:
        error_data = {
            "error": e.stderr
        }
        return jsonify(error_data), 200


if __name__ == '__main__':
    app.run(debug=True)

