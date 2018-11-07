'''
    创建应用程序，并注册相关蓝图
'''
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from app.models.base import db
from flask_cache import Cache
import os

login_manager = LoginManager()
mail = Mail()
cache = Cache()


def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    # 将注册好的蓝图注册到app对象中
    register_web_blueprint(app)

    # 将login_manager插件注册到app中
    login_manager.init_app(app)
    # 告诉login_manager哪个函数是登录视图函数
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    mail.init_app(app)
    # 将数据库注册到app对象中(其余插件的注册方式都是这样的)
    db.init_app(app)

    #将app对象中建好的数据模型映射到数据库中
    db.create_all(app=app)

    # 配置缓存
    cache.init_app(app)

    return app
