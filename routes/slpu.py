# routes/slpu.py
import random
from flask import Blueprint, Response

slpu_bp = Blueprint("slpu", __name__)

def simulate_game(board_size):
    players = [0, 0]
    dice_mode = ["normal", "normal"]
    rolls = []

    turn = 0
    last_square = board_size

    while True:
        player = turn % 2
        if dice_mode[player] == "normal":
            roll = random.randint(1, 6)
            if roll == 6:
                dice_mode[player] = "power2"
            move = roll
        else:
            roll = random.randint(1, 6)
            move = 2 ** roll
            if roll == 1:
                dice_mode[player] = "normal"

        # Move player
        players[player] += move

        # Bounce back if overshoot
        if players[player] > last_square:
            players[player] = last_square - (players[player] - last_square)

        # Add to rolls (just digits, no spaces)
        rolls.append(str(roll))

        # Win condition (last player must win)
        if players[player] == last_square and player == 1:
            break

        turn += 1

    return "".join(rolls)


@slpu_bp.route("/slpu", methods=["POST"])
def slpu():
    board_size = 16 * 16  # placeholder, later parse from input SVG
    rolls = simulate_game(board_size)
    # ✅ Only return <svg><text>...</text></svg>, nothing else
    return Response(
        f'<svg xmlns="http://www.w3.org/2000/svg"><text>{rolls}</text></svg>',
        mimetype="image/svg+xml"
    )
