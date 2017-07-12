# -*- coding: utf-8 -*-
"""
@Time : 2017/7/12 14:12
@Author : Yu Yuan

"""
from flask import Flask
from controller import register_controller


def create_app():
    app = Flask(__name__)
    register_controller(app)
    return app