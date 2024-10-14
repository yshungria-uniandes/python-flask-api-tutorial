from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de to-dos
todos_list = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# Endpoint para obtener todos los to-dos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos_list)

# Endpoint para agregar un nuevo to-do
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos_list.append(request_body)
    return jsonify(todos_list), 200

# Endpoint para eliminar un to-do por posición
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    if 0 <= position < len(todos_list):
        del todos_list[position]
    else:
        return jsonify({"error": "Invalid position"}), 400
    return jsonify(todos_list), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
