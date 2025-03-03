from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv

load_dotenv()

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)

from app import views
