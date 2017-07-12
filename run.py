# -*- coding: utf-8 -*-
"""
@Time : 2017/7/12 14:13
@Author : Yu Yuan

"""
from appmanage import create_app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
