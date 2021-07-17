from flask import Flask
from flask_restful import Api, Resource, reqparse
import sqlite3
import requests
from requests.api import request

from werkzeug.sansio.response import Response
from testsqlite3 import  put_bd, get_bd, post_bd, delete_bd, create_bd 
app = Flask(__name__)
api = Api(app)
#---База цитат---

#---Запрос на вывод цитат---
class Quote(Resource):
    create_bd()
    def get(self, id=None):
        """Вывод цитат."""
        return get_bd(id)
        
    #---Добавление цитат---
    def post(self):
        """Добавление цитат."""
        params = get_params('inp_author', 'inp_quote')
        return  post_bd(*params), 201
       
        
    #---Изменение цитат---
    def put(self, id):
        """Изменение цитат."""
        params = get_params('inp_author', 'inp_quote')
        return put_bd(*params, id)
       
        
    def delete(self, id):
        """Удаление цитат."""
        return delete_bd(id)
    
def get_params(*args):
    parser = reqparse.RequestParser()
    for param in args:
        parser.add_argument(param)
    return parser.parse_args().values()
        

api.add_resource(Quote, "/","/<int:id>", "/post/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)