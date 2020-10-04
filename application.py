#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import random
import json

from flask import Flask, request
from flask_restx import fields, Api, Resource

app = Flask(__name__)
api = Api(app)

todos = {}

model = api.model('ModelInput', {
    'data': fields.String(required=True)
})

model_output = api.model('ModelOutput', {
    'resource_name': fields.String(required=True),
    'resource_input': fields.String(required=True),
})

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    @api.expect(model)
    @api.marshal_with(model_output, 200)
    def put(self, todo_id):
        data = request.get_json()
        todos[todo_id] = data['data']
        return {
            'resource_name': todo_id,
            'resource_input': data['data']
        }

if __name__ == '__main__':
    app.run(debug=True)
