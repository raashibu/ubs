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
            move = roll
            if roll == 6:
                dice_mode[player] = "power2"
        else:
            roll = random.randint(1, 6)
            move = 2 ** roll
            if roll == 1:
                dice_mode[player] = "normal"

        rolls.append(str(roll))  # record die face, not move
        players[player] += move

        if players[player] > last_square:
            players[player] = last_square - (players[player] - last_square)

        if players[player] == last_square:
            break

        turn += 1

    return "".join(rolls)


@slpu_bp.route("/slpu", methods=["POST"])
def slpu():
    board_size = 16 * 16
    rolls = simulate_game(board_size)
    svg_output = f'<svg xmlns="http://www.w3.org/2000/svg"><text>{rolls}</text></svg>'
    return Response(svg_output, mimetype="image/svg+xml")
