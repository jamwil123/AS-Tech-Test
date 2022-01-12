from flask import Flask, jsonify, request
from Controllers.candidate_controller import create_candidate, make_score, fetch_candidates
from db import create_tables, make_db

app = Flask(__name__)


@app.route('/create-candidate', methods=["POST"])
def candidate_creation(): 
    candidate = request.get_json()
    name = candidate["name"]
    candidate_ref = candidate["candidate_ref"]
    result = create_candidate(name, candidate_ref)
    return jsonify(result)


@app.route('/create-score', methods=["PUT"])
def create_score(): 
    candidate = request.get_json()
    candidate_ref = candidate["candidate_ref"]
    score = candidate['score']
    result = make_score(candidate_ref, score)
    return jsonify(result)

@app.route('/get-candidates/<candidateRef>', methods=["GET"])
def get_candidates(candidateRef): 
    result = fetch_candidates(candidateRef)
    return jsonify(result)
    


if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=False)

