from flask import Flask, request, jsonify
from db import init_db, insert_game, get_games
import os

app = Flask(__name__)

# Inicializa o banco de dados
init_db()

@app.route('/heltz', methods=['GET'])
def heltz():
    return "OK", 200

@app.route('/games', methods=['POST'])
def add_game():
    data = request.get_json()
    name = data.get('name')
    release_date = data.get('release_date')
    genre = data.get('genre')
    
    if not name or not release_date or not genre:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    insert_game(name, release_date, genre)
    return jsonify({"message": "Game adicionado com sucesso!"}), 201

@app.route('/games', methods=['GET'])
def get_all_games():
    games = get_games()
    return jsonify(games), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
