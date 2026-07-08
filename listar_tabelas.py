import sqlite3

conn = sqlite3.connect("radar.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'pr_%';")
tabelas = cursor.fetchall()

print("Tabelas que começam com 'pr_':")
for t in tabelas:
    print(t[0])

conn.close()