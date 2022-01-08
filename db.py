import sqlite3 

DATABASE_NAME = 'candidates.db'


def make_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS candidates(
                name TEXT NOT NULL,
				candidate_ref TEXT NOT NULL,
				score INTEGER
            )
            """
    ]
    db = make_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)