# APITarefas
API para Gerenciar uma Lista de Tarefas

O objetivo deste projeto é me ajudar a fixar os comandos e as regras de criação de uma API usando Flask. Para isso, utilizarei um CRUD (Create, Read, Update, Delete) para gerenciar uma lista de tarefas.
# Tecnologias Ultilizadas:
* Flask: Framework web para Python , ultilizado para criar as rotas da API.
* SQLite: Banco de Dados relacional embutido, ultilizado para armazenar as tarefas.
* Python: Linguagem de programação ultilizada para desenvolver o backend da API.

# Instalação:
* 1. Clone o repositório
  git clone [text](https://github.com/Erivanialeal/APITarefas.git)
* 2. Instale as dependências:
  pip install -r requirements.txt
* 3. Inicialize o banco de dados: Antes de rodar a API, certifique-se de que o banco de dados está configurado. O SQLite será criado automaticamente quando voçê rodar o servidor pela primeira vez.
# Uso:
* Para rodar a API localmente, basta executar o seguinte comando:
 python app.py
 Isso irá iniciar o servidor da API no endereço http://127.0.0.1:5000/ 
# Rotas da API:
* POST/tarefas
* Descrição: Rota para criar tarefas.
* GET/listar_tarefa.
* Descrição: Lista todas as tarefas.
* GET//listar_id/<int:id>.
* Descrição: Retorna a tarefa com o id especifico.
* PUT/atualizar.
* Descrição: atualiza uma tarefa existente.
* DELETE/deletar_tarefa.
* Descrição: Deleta uma tarefa existente

# Contribuição:
* Se você quiser contribuir para esse projeto, sinta-se à vontade para fazer um fork do repositório, fazer alterações e enviar um pull request.

