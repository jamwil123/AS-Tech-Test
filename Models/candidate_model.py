from db import make_db

def insert_Candidate(name, candidate_ref): 
    db = make_db()
    cursor = db.cursor()
    statement = "INSERT INTO candidates(name, candidate_ref) VALUES (?, ?)"
    cursor.execute(statement, [name, candidate_ref])
    db.commit()

    statement = "SELECT * FROM candidates"
    cursor.execute(statement)
    return cursor.fetchall()