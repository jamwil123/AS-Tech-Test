from Models.candidate_model import insert_Candidate,  insert_score, retrieve_candidates
from db import create_tables, make_db

def create_candidate(name, candidateRef) : 
    data = insert_Candidate(name, candidateRef)
    return data


def make_score(candidate_ref, score): 
    data = insert_score(candidate_ref, score)
    return data

def fetch_candidates(candidateRef): 
    data = retrieve_candidates(candidateRef)
    print(data)
    return data
