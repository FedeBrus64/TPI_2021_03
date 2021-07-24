from flask import Flask
from config import Config
from .database.cliente_db import reset_table

from .routes import global_scope, api_scope, errors_scope

LibFyF = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
LibFyF.config.from_object(Config)

LibFyF.register_blueprint(global_scope, url_prefix="/")
LibFyF.register_blueprint(errors_scope, url_prefix="/")
LibFyF.register_blueprint(api_scope, url_prefix="/api")