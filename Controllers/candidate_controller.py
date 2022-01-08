from Models.candidate_model import insert_Candidate

def create_candidate(name, candidateRef) : 
    data = insert_Candidate(name, candidateRef)
    return data
