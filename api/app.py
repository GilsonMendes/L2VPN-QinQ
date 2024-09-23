from flask import Flask, jsonify, request
from netmiko import ConnectHandler
import json

app = Flask(__name__)


livros = [
    {
        'id': 1,
        'nome': 'Redes Kurose 1',
        'autor': 'Kurose 1',
        'ano_publicacao': 2020,
        'editora': 'Etica 1'
    },
    {
        'id': 2,
        'nome': 'Cisco 2',
        'autor': 'Netacademy 2',
        'ano_publicacao': 2021,
        'editora': 'Cisco Press'
    },
    {
        'id': 3,
        'nome': 'Cisco OSPF 2',
        'autor': 'Netacademy 2',
        'ano_publicacao': 2021,
        'editora': 'Cisco Press'
    },
]
#Consuktar todos
@app.route('/routers',methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
#Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)








#https://www.youtube.com/watch?v=FBLAV1SbJFk