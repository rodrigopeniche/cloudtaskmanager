# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask import render_template
import data_access

app = Flask(__name__)
api = Api(app)

@app.route('/')
def get():
    return render_template('login.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    data = []
    data.append(request.args.get('description'))
    data.append(request.args.get('urgency'))
    data.append(request.args.get('status'))
    data_access.insert(data)
    return ('added')

@app.route('/remove', methods=['POST', 'GET'])
def remove():
    data_access.delete(request.args.get('id'))
    return ('removed')

'''class Index(Resource):
    @app.route('/')
    def get(self):
        return render_template('login.html')'''

class Products(Resource):
    def get(self):
        return 'products'


#api.add_resource(Index, '/')
api.add_resource(Products, '/products')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')