from flask import Flask

from flasgger import Swagger
from flask_cors import CORS
from werkzeug.utils import import_string

from voxy.init_routes import init_routes


def create_app(config_class='DevConfig'):
    app = Flask(__name__)

    cfg = import_string(f'{__name__}.config.{config_class}')()
    app.config.from_object(cfg)
    app.config['CONFIG_CLASS'] = config_class

    cors = CORS(app, origins='{0}'.format(app.config.get('CORS_SUPPORTS_ORIGIN'))  # noqa: F841,E203
                , allow_headers=['Content-Type', 'Authorization', 'Access-Control-Allow-Credentials']  # noqa: E203
                , methods=['GET', 'POST', 'DELETE']  # noqa: E203
                , supports_credentials=True)

    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config["specs"] = [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ]

    swagger_config["static_url_path"] = "/flasgger_static"
    swagger_config["swagger_ui"] = True
    swagger_config["specs_route"] = "/api/apidocs/"
    swag = Swagger(app, config=swagger_config)  # noqa: F841

    init_routes(app)

    return app
