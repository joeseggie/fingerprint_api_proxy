from flask import Flask
import config
import os

def config_app(app):
    config_name = os.getenv('FLASK_ENV', 'default')
    app.config.from_pyfile('config.py')
    app.config.from_object(config_env[config_name])

app = Flask(__name__, instance_relative_config=True)
config_env = {
    'default': 'config.default.Config',
    'development': 'config.development.DevelopmentConfig',
    'production': 'config.production.ProductionConfig',
    'testing': 'config.testing.TestingConfig'
}
config_app(app)
