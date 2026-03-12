import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="workout_gen",
    user="workout_user",
    password="workout1234"
)

cur = conn.cursor()
cur.execute("SELECT * FROM Exercises WHERE goal='hypertrophy' AND difficulty='intermediate';")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()