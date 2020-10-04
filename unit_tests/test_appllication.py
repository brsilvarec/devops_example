
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import random
import json

from application import app

class TestApplication(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.headers = {'Content-type': 'application/json'}
        return super().setUp()

    def test_hello_world(self):
        """ Get hello world
        """
        path = '/hello'
        data = self.client.get(path)
        expected_response = {'hello': 'world'}
        assert expected_response == data.json
    
    def test_put_get(self):
        """ test application by putting a resource and reading it back
        """
        resource_name = "resource_test1"
        path = f'/{resource_name}'

        data = {
            "data": "Test data"
        }

        api_response = self.client.put(
            path,
            data=json.dumps(data),
            headers=self.headers
        )

        expected_response = {
            "resource_name": "resource_test1",
            "resource_input": "Test data"
        }

        # Test put
        assert expected_response == api_response.json, \
            "PUT Error: Response different from expected"
        
        api_response = self.client.get(
            path,
            headers=self.headers
        )

        expected_response = {
            "resource_test1" : "Test data"
        }

        # Test put
        assert expected_response == api_response.json, \
            "GET Error: different response from expected"
        