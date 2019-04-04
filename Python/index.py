# -*- coding: utf-8 -*-

from flask import Flask,jsonify,request
import testProcess


app = Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    return jsonify({'message' : 'text classification'})


@app.route('/classification', methods=['POST'])
def post():
    content = request.get_json()
    result = testProcess.main(content)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
