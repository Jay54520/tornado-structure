# -*- coding: utf-8 -*-
from tornado.testing import AsyncHTTPTestCase

from app import make_app


class CustomAsyncHTTPTestCase(AsyncHTTPTestCase):

    def get_app(self):
        return make_app()
