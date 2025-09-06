from flask import Blueprint, request, jsonify

sailing_bp = Blueprint("sailing_club", __name__)

def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # overlap
            merged[-1][1] = max(last[1], current[1])
        else:
            merged.append(current[:])  # copy to avoid mutation

    return merged

def min_boats(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))   # boat required
        events.append((end, -1))    # boat freed

    events.sort(key=lambda x: (x[0], x[1]))
    boats, max_boats = 0, 0
    for _, change in events:
        boats += change
        max_boats = max(max_boats, boats)
    return max_boats

@sailing_bp.route("/sailing-club/submission", methods=["POST"])
def sailing_submission():
    data = request.get_json()
    test_cases = data.get("testCases", [])

    solutions = []
    for case in test_cases:
        case_id = case["id"]
        intervals = [list(slot) for slot in case["input"]]

        merged = merge_intervals([slot[:] for slot in intervals])
        boats_needed = min_boats(intervals)

        solutions.append({
            "id": case_id,
            "sortedMergedSlots": merged,
            "minBoatsNeeded": boats_needed
        })

    return jsonify({"solutions": solutions})
