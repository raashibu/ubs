import xml.etree.ElementTree as ET

@slpu_bp.route("/slpu", methods=["POST"])
def slpu():
    svg_data = request.data.decode("utf-8")
    root = ET.fromstring(svg_data)

    # 1. Parse board size (example: from <svg height="..." width="..."> or metadata text)
    h = int(root.get("height", "16"))
    w = int(root.get("width", "16"))
    board_size = h * w

    # 2. Parse snakes and ladders
    snakes = {}
    ladders = {}
    for line in root.findall(".//{http://www.w3.org/2000/svg}line"):
        x1, y1, x2, y2 = [int(float(line.get(attr))) for attr in ("x1","y1","x2","y2")]
        # convert coordinates -> board squares
        # determine if it's a snake (downward) or ladder (upward)
        # fill snakes[head] = tail or ladders[bottom] = top

    # 3. Simulate game
    rolls = simulate_game(board_size, snakes, ladders)

    # 4. Return rolls as SVG
    svg_output = f'<svg xmlns="http://www.w3.org/2000/svg"><text>{rolls}</text></svg>'
    return Response(svg_output, mimetype="image/svg+xml")
