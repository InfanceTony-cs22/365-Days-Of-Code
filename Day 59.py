class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return []

        # Sort intervals based on start time
        intervals.sort(key=lambda x: x.start)

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            last_merged_interval = merged[-1]

            # If current interval overlaps with the last merged interval, merge them
            if current_interval.start <= last_merged_interval.end:
                last_merged_interval.end = max(last_merged_interval.end, current_interval.end)
            else:
                # If there's no overlap, add the current interval to the merged list
                merged.append(current_interval)

        return merged
