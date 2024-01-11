from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Ajoutez cette ligne pour activer le support CORS

@app.route('/mac')
def get_mac():
    elements = ['element 1', 'element 2', 'element 3']
    print("****************PULL_LIST*****************")
    return jsonify(elements)

@app.route('/add')
def add():
    elements = 200
    print("****************APAIRING*****************")
    return jsonify(elements)

@app.route('/open')
def open():
    elements = 200
    print("****************OPEN*****************")
    return jsonify(elements)

if __name__ == '__main__':
    port = 9001
    app.run(port=port, debug=True)
    print(f"Serveur en cours d execution sur le port {port}")
