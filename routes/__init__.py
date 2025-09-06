from flask import Flask
from routes.sailing_club import sailing_bp

app = Flask(__name__)
app.register_blueprint(sailing_bp)
