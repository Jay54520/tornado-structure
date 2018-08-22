# -*- coding: utf-8 -*-
from sample import handlers

url_patterns = [
    (r"/hello", handlers.HelloHandler),
    (r"/hi", handlers.HiHandler),
]
