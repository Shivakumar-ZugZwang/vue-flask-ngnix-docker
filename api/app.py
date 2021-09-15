from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify(msg='Hello World!')


@ app.route('/about')
def hello():
    return jsonify(msg='About!')


if __name__ == '__main__':
    app.run(debug=True)
