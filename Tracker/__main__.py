from flask import Flask
from waitress import serve
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.debug = False
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from . import routes
        from .inserts import insert_data
        db.create_all()
        insert_data(db)

        return app


if __name__ == '__main__':
    app = create_app()
    serve(app, host='0.0.0.0', port=8000)
