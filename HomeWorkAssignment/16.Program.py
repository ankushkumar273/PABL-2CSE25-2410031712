def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        # Check if current interval overlaps with last merged interval
        if current[0] <= last[1]:
            # Merge intervals
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged
