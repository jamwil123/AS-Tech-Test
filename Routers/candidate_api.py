from flask import Flask, jsonify, request
from db import create_tables
import create_candidate 
create_candidate.path.append('TechTestAS/Controllers/candiate_controller.py')

app = Flask(__name__)

@app.route('/games', methods=["GET"])
    create_candidate()
