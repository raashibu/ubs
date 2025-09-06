# routes/slpu.py
import random
from flask import Blueprint, Response, request

slpu_bp = Blueprint("slpu", __name__)   # 👈 must exist at module level

def simulate_game(board_size, snakes=None, ladders=None):
    # ... your simulate logic here ...
    return "12345"

@slpu_bp.route("/slpu", methods=["POST"])
def slpu():
    board_size = 16 * 16
    rolls = simulate_game(board_size)
    svg_output = f'<svg xmlns="http://www.w3.org/2000/svg"><text>{rolls}</text></svg>'
    return Response(svg_output, mimetype="image/svg+xml")
