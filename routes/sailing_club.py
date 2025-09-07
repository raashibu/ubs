from flask import Flask, Blueprint, request, jsonify

# Create a Blueprint with a prefix "/sailing-club"
sailing_bp = Blueprint("sailing_club", __name__, url_prefix="/sailing-club")

# Function to merge intervals
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0][:]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current[:])
    return merged

# Function to calculate min number of boats
def min_boats(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    events.sort(key=lambda x: (x[0], x[1]))
    boats = max_boats = 0
    for _, change in events:
        boats += change
        max_boats = max(max_boats, boats)
    return max_boats

# Define the endpoint at POST /sailing-club/submission
@sailing_bp.route("/submission", methods=["POST"])
def sailing_submission():
    try:
        data = request.get_json(force=True)
        test_cases = data.get("testCases", [])

        solutions = []
        for case in test_cases:
            cid = case["id"]
            intervals = [list(slot) for slot in case["input"]]

            merged = merge_intervals(intervals[:])
            boats_needed = min_boats(intervals)

            solutions.append({
                "id": cid,
                "sortedMergedSlots": merged,
                "minBoatsNeeded": boats_needed
            })

        return jsonify({"solutions": solutions}), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 400

# Register blueprint and start the app
app = Flask(__name__)
app.register_blueprint(sailing_bp)

if __name__ == "__main__":
    app.run(debug=True)
