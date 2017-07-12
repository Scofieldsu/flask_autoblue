# -*- coding: utf-8 -*-
"""
@Time : 2017/7/12 14:08
@Author : Yu Yuan

"""
import logging
import multiprocessing
import os
import time

FORMAT = (
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
)
basedir = os.path.abspath(os.path.dirname(__file__))
logsdir = os.path.join(basedir, "../logs")


class Logger(object):
    def __init__(self, app=None):
        self.app = app

        self.logger = None
        self.daytime = time.strftime("%Y%m%d")
        self.filename = logsdir + "/log.log"
        self.handler = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.logger = app.logger
        self.add_file_handler()

    def change_daytime(self, nowtime):
        self.daytime = nowtime
        self.filename = logsdir + "log.log"
        self.logger.removeHandler(self.handler)
        self.add_file_handler()

    def add_file_handler(self):
        if self.handler:
            self.logger.removeHandler(self.handler)
        if self.filename:
            from logging.handlers import TimedRotatingFileHandler
            self.handler = TimedRotatingFileHandler(self.filename, when='D')
            formatter = logging.Formatter(FORMAT)
            self.handler.setFormatter(formatter)
            self.handler.setLevel(logging.DEBUG)
            self.logger.addHandler(self.handler)