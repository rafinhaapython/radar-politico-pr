import sqlite3

conn = sqlite3.connect("radar.db")
cursor = conn.cursor()

# Lista todas as tabelas criadas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

print("Tabelas encontradas no banco:")
for t in tabelas:
    print(t[0])

conn.close()