from flask import Flask, request
from flask_restful import Resource, Api, reqparse

import json
import os


app = Flask(__name__)
api = Api(app)

file_path = os.path.abspath(os.path.join('data.json'))

with open(file_path) as f:
    items = json.load(f) # data of json file




class Item(Resource):
#    @jwt_required() # for authenticate
    def get(self, title):
        item = next(filter(lambda x: x['title'] == title,items ), None)
        return {'item': item}, 200 if item else 404

    def post(self, title):
        if next(filter(lambda x: x['title'] == title,items ), None): #if we found an item which is not none
            return {'message': "An item with name {} already exist".format(title)}, 400

        data = request.get_json()
        item = {'title': title,
        'summary':data['summary'],
        'content': data['content'],
        'published_status': data['published_status'],
        'published_date': data['published_date'],
        'category': data['category'],
        'author': data['author'] }


        items.append(item)
        with open(file_path, 'w') as f:
            json.dump(items, f)
        return item, 201 # code 201 for returned ok


    def delete(self, title):
        global items
        items = list(filter(lambda x: x['title'] != title, items))
        with open(file_path, 'w') as f:
            json.dump(items, f)
        return {'message': 'Item delete'}

    def put(self,title):  # WORK IS HERE
        item = next(filter(lambda x: x['title'] == title, items), None)
        if item is None:
            item = {'title': name, 'price': data['price']}
            item.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:title>') # http:127.0.0.1:5000/item/rolf
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
