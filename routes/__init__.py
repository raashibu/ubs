from flask import Flask
from .slpu import slpu_bp

app = Flask(__name__)
app.register_blueprint(slpu_bp)
