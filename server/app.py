from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import Config

# Initialize extensions
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Import models for migration
from server.models import *

# Register blueprints
from server.controllers.guest_controller import guest_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.appearance_controller import appearance_bp
from server.controllers.auth_controller import auth_bp

app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return {'message': 'Late Show API is running!'}
