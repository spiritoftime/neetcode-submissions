class Solution {
    public int binarySearch(int[][] intervals, int[] newInterval) {
        int l = 0;
        int r = intervals.length - 1;
        int newStart = newInterval[0];
        while (l <= r) {
            int m = (l + r) / 2;
            int currStart = intervals[m][0];
            if (currStart == newStart) {
                return m;
            } else if (currStart < newStart) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return l;
    }

    public int[] mergeTwoIntervals(int[] i1, int[] i2) {
        i2[0] = Math.min(i1[0], i2[0]);
        i2[1] = Math.max(i1[1], i2[1]);
        return i2;
    }

    // Merges the intervals and returns new intervals array
    public int[][] expandOutwards(int indexToExpandFrom, int[] newInterval, int[][] intervals) {
        int[] merged = new int[] { newInterval[0], newInterval[1] };
        int l = indexToExpandFrom;
        int r = indexToExpandFrom;

        // Expand left
        while (l > 0 && merged[0] <= intervals[l - 1][1]) {
            merged = mergeTwoIntervals(intervals[l - 1], merged);
            l--;
        }

        // Expand right
        while (r < intervals.length && merged[1] >= intervals[r][0]) {
            merged = mergeTwoIntervals(intervals[r], merged);
            r++;
        }

        ArrayList<int[]> out = new ArrayList<>();
        // Add intervals before the merged interval
        for (int i = 0; i < l; i++) {
            out.add(intervals[i]);
        }

        // Add the merged interval
        out.add(merged);

        // Add intervals after the merged interval
        for (int i = r; i < intervals.length; i++) {
            out.add(intervals[i]);
        }

        return out.toArray(new int[out.size()][]);
    }

    public int[][] insert(int[][] intervals, int[] newInterval) {
        if (intervals.length == 0) {
            return new int[][] { newInterval }; // Handle edge case of empty intervals
        }
        int indexToExpandFrom = binarySearch(intervals, newInterval);
        return expandOutwards(indexToExpandFrom, newInterval, intervals);
    }
}
