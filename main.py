from flask import Flask, jsonify, request
from Controllers.candidate_controller import create_candidate
from db import create_tables

app = Flask(__name__)


@app.route('/create-candidate', methods=["POST"])
def candidate_creation(): 
    candidate = request.get_json()
    name = candidate["name"]
    candidate_ref = candidate["candidate_ref"]
    result = create_candidate(name, candidate_ref)
    return jsonify(result)


if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=False)

