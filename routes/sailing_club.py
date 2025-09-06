@sailing_bp.route("/sailing-club/submission", methods=["POST"])
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
        # Always return JSON, never HTML
        return jsonify({"error": str(e)}), 400
