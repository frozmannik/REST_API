from flask import Flask, request
from flask_restful import Resource, Api, reqparse
#from flask_admin import Admin  # dont have enough time to make a nice gui with it ( use postman instead)

import json
import os


app = Flask(__name__)
api = Api(app)
admin = Admin(app)

# storage of news ( could be replacsed by database )
file_path = os.path.abspath(os.path.join('data.json'))
with open(file_path) as f:
    items = json.load(f)

class Item(Resource):

    # parse a file with a checking of each field
    parser = reqparse.RequestParser()
    parser.add_argument('title',type = str, required=True, help ="This field cannot be empty")
    parser.add_argument('summary',type = str, required=True, help ="This field cannot be empty")
    parser.add_argument('content',type = str, required=True, help ="This field cannot be empty")
    parser.add_argument('published_status',type = bool, required=True, help ="This field cannot be empty") # WHAT IS published status??? is it boolean value? if not Change it here
    parser.add_argument('published_date',type = str, required=True, help ="This field cannot be empty") # using string just to make it simplier here late will be changed to datatime
    parser.add_argument('category',type = str, required=True, help ="This field cannot be empty")
    parser.add_argument('author',type = str, required=True, help ="This field cannot be empty")

    def get(self, title):
        item = next(filter(lambda x: x['title'] == title,items ), None)  # function to find specific field
        return {'item': item}, 200 if item else 404  # if successfully added return status 200(OK) if not 404(NOT FOUND)

    def post(self, title):
        if next(filter(lambda x: x['title'] == title,items ), None): #if we found an item which is not none
            return {'message': "An item with name {} already exist".format(title)}, 400  # if item already exist don't post it and return 400(BAD request)

        #adding a item to db
        data = Item.parser.parse_args()
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
        return {'message': 'Item delete'}, 200

    def put(self,title):  # update exsisting news
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['title'] == title, items), None)

        if item is None:
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
        else:
            item.update(data), 200 # 200 for OK , can be replaced on 201 for created, not a big deal here
        return item, 201 # 201 for creted

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:title>') # http:127.0.0.1:5000/item/titel1
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=False) # change debug on True for debugin
