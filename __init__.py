# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/25 15:24
# @Author : '红文'
# @File : __init__.py
# @Software: PyCharm
from flask import Flask
from app.models.book import db
from flask_login import login_manager, LoginManager

login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或者注册'

    mail.init_app(app)

    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
