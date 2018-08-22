# -*- coding: utf-8 -*-
import json
import tornado.web
import tornado.web
from json import JSONDecodeError
from tornado.escape import json_decode

from sample import constants


class BaseHandler(tornado.web.RequestHandler):

    def prepare(self):
        """only deal json"""
        try:
            json_data = json_decode(self.request.body)
        except JSONDecodeError:
            self.write_json('invalid JSON', 400)
            self.finish()
        else:
            self.request.arguments = json_data

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def write_json(self, data, status=200):
        self.set_status(status)
        self.write(json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))


class HelloHandler(BaseHandler):
    def post(self):
        self.create_hello()
        self.write_json("{}, {}".format(constants.HELLO, self.request.arguments))

    def create_hello(self):
        pass


class HiHandler(BaseHandler):
    def post(self):
        self.create_hi()
        self.write_json("{}, {}".format(constants.Hi, self.request.arguments))

    def create_hi(self):
        pass
