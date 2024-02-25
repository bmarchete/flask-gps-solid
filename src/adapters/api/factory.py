from flask import Flask

from adapters.api.blueprints.routes_bp import routes_bp

# Define blueprints
blueprints = [routes_bp]

def create():
    app = Flask("flask-api")

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app