from flask import Flask
from database import init_db
from routes import tarefa_routes

app=Flask(__name__)
#inicializa o banco de dados e cria a tabela
init_db()
#registro do Blueprintno aplicativo principal
app.register_blueprint(tarefa_routes)
if __name__== '__main__':
    app.run(debug=True)