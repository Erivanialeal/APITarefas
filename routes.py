from flask import Blueprint, request, jsonify
import datetime
from database import inserir_tarefa,listar_tarefa,listar_por_id,atualizar_tarefa,Tarefa

# Definindo o blueprint para as rotas de tarefas
tarefa_routes = Blueprint('tarefa_routes', __name__)

@tarefa_routes.route('/tarefas',methods=['POST'])
def criar_tarefa():
    data=request.get_json() #Recebe os dados enviado pelo cliente
    #extrair os dados
    descricao=data.get('descricao')
    titulo=data.get('titulo')
    concluido=data.get('concluido')

    #verificar se a descição foi fornecida
    if not descricao or not titulo or  concluido is None:
        return jsonify({'Erro':'Descrição, titulo, concluido é obrigatoria'}),400
    try:
        inserir_tarefa(descricao,titulo,concluido)
        return jsonify({'mensagem':'Tarefa criada com sucesso!'}),201
    except Exception as e:
        return jsonify({'erro':'Erro ao criar tarefa. ','details':str(e)}),500
@tarefa_routes.route('/listar_tarefa',methods=['GET'])
def listar():
    try:
        tarefas=listar_tarefa()#chama a função para buscar tarefa
        print(tarefas) #print para debug
        lista_formatada=[]
        for tarefa in tarefas:
            lista_formatada.append({
                'id':tarefa[0],
                'descricao':tarefa[1],
                'titulo':tarefa[2],
                'concluido':tarefa[3],
                'data_criacao':tarefa[4]
            })
        #retorna a lista formatada em formato json
        return jsonify(lista_formatada)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500 #retorna um erro em caso de exceção
        

@tarefa_routes.route('/listar_id/<int:id>',methods=['GET'])
def listar_uma_tarefa(id):#recebe o id da url
    tarefa=listar_por_id(id) #chamando a função de database.py com o id fornecido
    if tarefa:
        return({
            'id':tarefa[0],
            'descricao':tarefa[1],
            'titulo':tarefa[2],
            'concluido':tarefa[3],
            'data_criacao':tarefa[4]
        })
    else:
        return jsonify({'mensagem':'Tarefa não encontrada'}),404 #não encontrada
@tarefa_routes.route('/atualizar/<int:id>',methods=['PUT'])
def atualizar_tarefa_route(id):
    dados=request.get_json() #recuperando o json da requisição
    if not dados:
        return jsonify({"erro":"Dados inválidos"}),400 
    
    descricao= dados.get('descricao')
    titulo=dados.get('titulo')
    concluido=dados.get('concluido')
    # chamar a função do banco de dados para atualizar tarefa
    tarefa_atualizada=atualizar_tarefa(id,descricao,titulo,concluido)
    if not tarefa_atualizada:
        return jsonify({'erro':'tarefa não encontrada'}),404
    
    return jsonify({
            "id": id,
            "titulo": titulo,
            "descricao": descricao,
            "concluido": concluido
        
    }), 200
@tarefa_routes.route('/deletar_tarefa/<int:id>', methods=['DELETE'])
def Deletar_tarefa(id):
    print(f"Recebendo requisição para deletar a tarefa com ID: {id}")
    resultado=Tarefa(id)
    print(resultado)
    if resultado is None:
        return jsonify({"erro":"Tarefa não encontrada"}),404 #tarefa não encontrada
    return '',204 #caso a exclusão seja bem-sucedida
    




    
    
    