import sqlite3

DATABASE_NAME = 'candidates.db'


def make_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """DROP TABLE IF EXISTS candidates""", 
        """DROP TABLE IF EXISTS scores""",
        """CREATE TABLE IF NOT EXISTS candidates(
                name TEXT NOT NULL,
				candidate_ref VARCHAR(8) PRIMARY KEY UNIQUE NOT NULL,
				score INTEGER
            )
             """, 
             """CREATE TABLE IF NOT EXISTS scores(
                candidate_ref VARCHAR(8) REFERENCES candidates(candidate_ref),
				score INT(100)
            )
            """

    ]

    otherTable = []
    db = make_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
