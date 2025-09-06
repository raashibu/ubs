from flask import Flask
from routes.trivia import trivia_bp
from slpu import slpu_bp   # 👈 import the blueprint

app = Flask(__name__)
app.register_blueprint(trivia_bp)
app.register_blueprint(slpu_bp)  # 👈 register it
