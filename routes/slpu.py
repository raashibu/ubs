def simulate_game(board_size, snakes=None, ladders=None):
    players = [0, 0]
    dice_mode = ["normal", "normal"]
    rolls = []

    turn = 0
    last_square = board_size

    snakes = snakes or {}
    ladders = ladders or {}

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

        # record the actual die face, not the move
        rolls.append(str(roll))

        # move player
        players[player] += move

        # bounce back
        if players[player] > last_square:
            players[player] = last_square - (players[player] - last_square)

        # snakes/ladders
        if players[player] in snakes:
            players[player] = snakes[players[player]]
        elif players[player] in ladders:
            players[player] = ladders[players[player]]

        # win check
        if players[player] == last_square:
            break

        turn += 1

    return "".join(rolls)
