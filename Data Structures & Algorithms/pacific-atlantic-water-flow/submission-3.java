
// instead of flowing from current cell to the oceans, flow from ocean to as many cells as possible.

class Solution {
    private Set<Pair<Integer, Integer>> atlanticCoords = new HashSet<>();
    private Set<Pair<Integer, Integer>> pacificCoords = new HashSet<>();
    private int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}; // Down, Up, Right, Left

    private void flowWater(int[][] heights, Set<Pair<Integer, Integer>> oceanCoords,
                           int prevHeight, int currRowIndex, int currColIndex, boolean[][] visited) {
        // Out of bounds or already visited
        if (currRowIndex < 0 || currColIndex < 0 || currRowIndex >= heights.length || currColIndex >= heights[0].length
                || visited[currRowIndex][currColIndex] || heights[currRowIndex][currColIndex] < prevHeight) {
            return;
        }

        // Mark the cell as visited
        visited[currRowIndex][currColIndex] = true;
        oceanCoords.add(new Pair<>(currRowIndex, currColIndex));

        // Attempt to flow in all directions
        for (int[] dir : directions) {
            flowWater(heights, oceanCoords, heights[currRowIndex][currColIndex],
                      currRowIndex + dir[0], currColIndex + dir[1], visited);
        }
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int rows = heights.length;
        int cols = heights[0].length;

        boolean[][] pacificVisited = new boolean[rows][cols];
        boolean[][] atlanticVisited = new boolean[rows][cols];

        // Traverse from the borders for both oceans
        for (int r = 0; r < rows; r++) {
            // Pacific (left edge)
            flowWater(heights, pacificCoords, Integer.MIN_VALUE, r, 0, pacificVisited);
            // Atlantic (right edge)
            flowWater(heights, atlanticCoords, Integer.MIN_VALUE, r, cols - 1, atlanticVisited);
        }

        for (int c = 0; c < cols; c++) {
            // Pacific (top edge)
            flowWater(heights, pacificCoords, Integer.MIN_VALUE, 0, c, pacificVisited);
            // Atlantic (bottom edge)
            flowWater(heights, atlanticCoords, Integer.MIN_VALUE, rows - 1, c, atlanticVisited);
        }

        // Collect coordinates reachable by both oceans
        List<List<Integer>> result = new ArrayList<>();
        for (Pair<Integer, Integer> coord : pacificCoords) {
            if (atlanticCoords.contains(coord)) {
                result.add(List.of(coord.getKey(), coord.getValue()));
            }
        }

        return result;
    }
}
