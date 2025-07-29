import sqlite3

con = sqlite3.connect('database/telco_churn.db')
cur = con.cursor()
cur.execute('''
SELECT * FROM fact_table LIMIT 5''')
rows = cur.fetchall()

for row in rows:
    print(row)