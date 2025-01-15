import sqlite3
from datetime import datetime


def init_db():
    with sqlite3.connect('tarefas.db') as conn:
        cursor= conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS banco_tarefas(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       descricao TEXT NOT NULL,
                       titulo TEXT NOT NULL,
                       concluido BOOLEAN NOT NULL DEFAULT 0,
                       data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                       )
''')
        conn.commit()
    #init_db()
    print("Banco de dados e tabelas banco_tarefas criado com sucesso")
def inserir_tarefa(descricao,titulo,concluido,data_criacao=None):
    #definir a data de criação da tarefa
    if data_criacao is None:
        data_criacao=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("Inserindo dados:", descricao, titulo, concluido, data_criacao)
    try:
        with sqlite3.connect('tarefas.db') as conn:
            cursor=conn.cursor()
            cursor.execute("INSERT INTO banco_tarefas (descricao,titulo,concluido,data_criacao)VALUES (?,?,?,?)",(descricao,titulo,concluido,data_criacao))

        conn.commit()
    except sqlite3.Error as e:
        print("Erro ao inserir tarefas",e)
def listar_tarefa():
         conn=sqlite3.connect('tarefas.db')
         cursor=conn.cursor()
         cursor.execute("SELECT id,descricao,titulo,concluido,data_criacao FROM banco_tarefas")
         tarefa= cursor.fetchall() #fetchall coleta todos os registros
         conn.close()
         return tarefa
def listar_por_id(id):
     conn=sqlite3.connect('tarefas.db')
     cursor=conn.cursor()
     cursor.execute("SELECT * FROM banco_tarefas WHERE id = ?", (id,))
     tarefa= cursor.fetchone()#coleta apenas 1 registro
     conn.close()
     return tarefa
def atualizar_tarefa(id,descricao=None,titulo=None,concluido=None):
    conn=sqlite3.connect('tarefas.db')
    cursor=conn.cursor()
    #verifica se a tarefa existe
    cursor.execute("SELECT * FROM banco_tarefas WHERE id = ?", (id,))
    tarefa=cursor.fetchone()
    if not tarefa:
        conn.close()
        return None
     
    # Atualiza somente os campos fornecidos
    if descricao is not None:
        cursor.execute("UPDATE banco_tarefas SET descricao = ? WHERE id = ?", (descricao, id))
    if titulo is not None:
        cursor.execute("UPDATE banco_tarefas SET titulo = ? WHERE id = ?", (titulo, id))
    if concluido is not None:
        cursor.execute("UPDATE banco_tarefas SET concluido = ? WHERE id = ?", (concluido, id))

    conn.commit()

    # Busca a tarefa atualizada
    cursor.execute("SELECT * FROM banco_tarefas WHERE id = ?", (id,))
    tarefa_atualizada = cursor.fetchone()

    conn.close()
    return tarefa_atualizada
def Tarefa(id):
    try:
        print(f"tentando deletar tarefa com o id {id}")
        conn=sqlite3.connect('tarefas.db')
        cursor=conn.cursor()
        #verificar se a tarefa existe
        cursor.execute('SELECT * FROM banco_tarefas WHERE id = ?',(id,))
        tarefa=cursor.fetchone()
        if not tarefa:
            print(f"Tarefa com ID {id} não encontrada.")
            return None
    
        cursor.execute("DELETE FROM banco_tarefas WHERE id= ?",(id,))
        print(f"Tarefa com ID {id} deletada com sucesso.")  # Confirma a exclusão
        conn.commit()#commit da transação
        return True #indica que a tarefa foi deletada com sucesso
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return False  # Retorna False em caso de erro

    finally:
        conn.close()  # Sempre fecha a conexão com o banco de dados