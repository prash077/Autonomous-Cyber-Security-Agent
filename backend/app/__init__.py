import os
from flask import Flask
from dotenv import load_dotenv
from .database import init_db

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    
    init_db(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app