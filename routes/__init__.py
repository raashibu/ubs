from flask import Flask
from .slpu import slpu_bp   # 👈 note the dot

app = Flask(__name__)
app.register_blueprint(slpu_bp)
