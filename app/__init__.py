from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object(Config)
toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models # noqa: E402
