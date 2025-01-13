from flask import Flask
from app.models.database import db
from app.controllers.data_controller import data_bp
from app.controllers.health_controller import register_health_routes
from app.errors import register_error_handlers
import os

def create_app():

    #Start Flask
    app = Flask(__name__)
    
    #Config DB
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    #Register errors handlers
    register_error_handlers(app)
    

    db.init_app(app)
    
    app.register_blueprint(data_bp)
    register_health_routes(app)

    return app