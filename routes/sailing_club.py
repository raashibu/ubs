from flask import Flask, Blueprint, request, jsonify

# Create a Blueprint
sailing_bp = Blueprint("sailing_club", __name__)

# Merge overlapping intervals
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

# Calculate minimum number of boats required (overlapping intervals)
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

# Route to handle submission
@sailing_bp.route("/sailing-club/submission", methods=["POST"])
def sailing_submission():
    try:
        # Get JSON body from request
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
        print("Exception occurred:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 400

# Run as standalone Flask app for testing
if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(sailing_bp)

    app.run(debug=True)
