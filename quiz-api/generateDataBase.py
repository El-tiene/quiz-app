import sqlite3

def create_database_schema():
    conn = sqlite3.connect('MyDataBase.db')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS question')
    cursor.execute('DROP TABLE IF EXISTS possibleAnswers')
    cursor.execute('DROP TABLE IF EXISTS participationResult')

    cursor.execute('''CREATE TABLE "participationResult" (
	"id"	INTEGER,
	"playerName"	TEXT NOT NULL,
	"score"	INTEGER NOT NULL,
	"date"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
)''')

    cursor.execute("""
        CREATE TABLE "possibleAnswers" (
	"id"	INTEGER NOT NULL,
	"text"	TEXT NOT NULL,
	"isCorrect"	TEXT NOT NULL,
	"positionquestion"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)
    """)

    cursor.execute("""
        CREATE TABLE "question" (
	"id"	INTEGER,
	"title"	TEXT NOT NULL,
	"position"	INTEGER NOT NULL,
	"text"	TEXT NOT NULL,
	"image"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)
    """)

    

    conn.commit()
    conn.close()
    return 'Ok',200
