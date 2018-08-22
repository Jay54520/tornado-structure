# -*- coding: utf-8 -*-
import json

from sample import constants
from sample.utils.test import CustomAsyncHTTPTestCase


class TestHelloHandler(CustomAsyncHTTPTestCase):

    def test_hello_world(self):
        world = 'world'
        response = self.fetch(
            '/hi',
            method='POST',
            body=json.dumps(world)
        )
        self.assertEqual(200, response.code)
        self.assertEqual('{}, {}'.format(constants.Hi, world), json.loads(response.body.decode()))