from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    from .routes.recipients import bp
    from .routes.messaging import messagingBp
    app.register_blueprint(bp)
    app.register_blueprint(messagingBp)

    with app.app_context():
        db.create_all()

    return app