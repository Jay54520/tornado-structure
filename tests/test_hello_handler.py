# -*- coding: utf-8 -*-
import json

from sample import constants
from sample.utils.test import CustomAsyncHTTPTestCase


class TestHelloHandler(CustomAsyncHTTPTestCase):

    def test_invalid_json(self):
        response = self.fetch(
            '/hello',
            method='POST',
            body='{[]: []}'
        )
        self.assertEqual(400, response.code)
        self.assertEqual('invalid JSON', json.loads(response.body.decode()))

    def test_hello_world(self):
        world = 'world'
        response = self.fetch(
            '/hello',
            method='POST',
            body=json.dumps(world)
        )
        self.assertEqual(200, response.code)
        self.assertEqual('{}, {}'.format(constants.HELLO, world), json.loads(response.body.decode()))