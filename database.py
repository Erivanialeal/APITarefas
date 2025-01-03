import sqlite3
from datetime import datetime

def init_db():
    with sqlite3.connect('tarefas.db') as conn:
        cursor= conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS banco_tarefas(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       descricao TEXT,
                       titulo TEXT,
                       concluido BOOLEAN NOT NULL DEFAULT 0,
                       data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                       )
''')
        conn.commit()
        print("Banco de dados e tabelas banco_tarefas criado com sucesso")
def inserir_tarefa(descricao,titulo=None):
    #definir a data de criação da tarefa
    data_criacao=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with sqlite3.connect('tarefas.db') as conn:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO banco_tarefas (descricao,titulo,data_criacao)VALUES (?,?,?)",(descricao,titulo,data_criacao))

        conn.commit()

