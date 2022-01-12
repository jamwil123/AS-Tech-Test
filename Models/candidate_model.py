from db import make_db

def insert_Candidate(name, candidate_ref): 
    db = make_db()
    cursor = db.cursor()
    statement = "INSERT INTO candidates(name, candidate_ref) VALUES (?, ?)"
    cursor.execute(statement, [name, candidate_ref])
    db.commit()

    statement = "INSERT INTO scores(candidate_ref) VALUES (?)"
    cursor.execute(statement, [candidate_ref])
    db.commit()

    statement = "SELECT * FROM candidates"
    cursor.execute(statement)
    return cursor.fetchall()

def insert_score(candidate_ref, score): 
    db = make_db()
    cursor = db.cursor()
    statement = "UPDATE scores SET score = (?) WHERE candidate_ref = (?)"
    cursor.execute(statement, [score, candidate_ref])
    db.commit()
    return cursor.fetchall()

def retrieve_candidates(candidateRef):
    db = make_db()
    cursor = db.cursor()
    statement = "SELECT * FROM candidates WHERE candidate_ref = (?)"
    cursor.execute(statement, [candidateRef])
    db.commit()
    return cursor.fetchall()


