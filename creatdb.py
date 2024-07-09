import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Criação da tabela de fotos
c.execute('''
    CREATE TABLE fotos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL
    )
''')

# Criação da tabela de usuários
c.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("Banco de dados criado com sucesso.")
