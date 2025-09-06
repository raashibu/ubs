from flask import Flask
from slpu import slpu_bp   # import your blueprint from slpu.py

app = Flask(__name__)
app.register_blueprint(slpu_bp)  # register only this one
