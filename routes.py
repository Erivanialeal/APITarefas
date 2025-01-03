from flask import Blueprint, request, jsonify
import datetime
from database import inserir_tarefa

# Definindo o blueprint para as rotas de tarefas
tarefa_routes = Blueprint('tarefa_routes', __name__)

@tarefa_routes.route('/tarefas',methods=['POST'])
def criar_tarefa():
    data=request.get_json() #Recebe os dados enviado pelo cliente
    #extrair os dados
    descricao=data.get('descrição')
    #verificar se a descição foi fornecida
    if not descricao:
        return jsonify({'Erro':'Descrição é obrigatoria'}),400
    try:
        inserir_tarefa(descricao)
        return jsonify({'mensagem':'Tarefa criada com sucesso!'}),201
    except Exception as e:
        return jsonify({'erro':'Erro ao criar tarefa. ','details':str(e)}),500

    
    
    