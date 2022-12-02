import sqlite3
con = sqlite3.connect("Percorso.db")
cur = con.cursor()
res = cur.execute(f"SELECT Movimento FROM Percorso WHERE ID = {id}")
res.fetchone()