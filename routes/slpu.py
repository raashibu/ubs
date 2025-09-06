import random
from flask import Flask, request, Response

app = Flask(__name__)

def simulate_game(board_size):
    """
    Simulate Snakes & Ladders Power Up! for 2 players.
    Returns the sequence of dice rolls as a string.
    """
    players = [0, 0]  # starting positions (before square 1)
    dice_mode = ["normal", "normal"]  # normal or power2 die
    rolls = []

    turn = 0
    last_square = board_size

    while True:
        player = turn % 2
        if dice_mode[player] == "normal":
            roll = random.randint(1, 6)
            if roll == 6:
                dice_mode[player] = "power2"
        else:
            roll = random.randint(1, 6)
            move = 2 ** roll
            if roll == 1:
                dice_mode[player] = "normal"
            roll = move

        # Move player
        players[player] += roll

        # Bounce back if overshoot
        if players[player] > last_square:
            players[player] = last_square - (players[player] - last_square)

        # Add to rolls
        rolls.append(str(roll))

        # Win condition
        if players[player] == last_square and player == 1:  # last player must win
            break

        turn += 1

    return "".join(rolls)


@app.route("/slpu", methods=["POST"])
def slpu():
    # Example: assume board size from <svg>, here just fixed 16x16
    board_size = 16 * 16

    rolls = simulate_game(board_size)

    # Return as SVG <text>
    svg_output = f'<svg xmlns="http://www.w3.org/2000/svg"><text>{rolls}</text></svg>'
    return Response(svg_output, mimetype="image/svg+xml")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
