from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    x = data['x']
    y = data['y']
    return jsonify({'result': x + y})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    x = data['x']
    y = data['y']
    return jsonify({'result': x * y})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
