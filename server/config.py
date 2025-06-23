import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Leon20@localhost:5432/late_show_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'super-secret-key')
