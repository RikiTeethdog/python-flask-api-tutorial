from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()  #Convert the request to a Python dictionary
    print("Incoming request with the following body:", request_body)

    todos.append(request_body)  #Add the new task to the global list

    return jsonify(todos)  #Return the updated list in JSON format

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)

    if 0 <= position < len(todos):  # 🔹 Verificamos que la posición es válida
        del todos[position]  # 🔹 Eliminamos la tarea con `del`
    else:
        return jsonify({"error": "Invalid position"}), 400

    return jsonify(todos)  # 🔹 Retornamos la lista actualizada


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)