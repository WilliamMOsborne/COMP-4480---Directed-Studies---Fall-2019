"""
Quick program to add crimes into the database
"""
import csv
import psycopg2


conn = psycopg2.connect(host="localhost",database="DirectedStudiesFall2019", user="postgres", password="REDACTED")

cur = conn.cursor()
with open('random_blocks_with_location.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO random_with_location  VALUES (%s, %s, %s, %s,%s, %s, %s)",
        row
        )
conn.commit()

