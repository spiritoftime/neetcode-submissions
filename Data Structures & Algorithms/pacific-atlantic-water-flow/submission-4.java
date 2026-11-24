class Solution {

    // instead of flowing from current cell to water, start from the oceans
    // and attempt to flow to as many cells as possible.
    private int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    private HashSet<Pair<Integer,Integer>> pacificCells = new HashSet<>();
    private HashSet<Pair<Integer,Integer>> atlanticCells = new HashSet<>();
    private  int rows;
    private  int cols ;

    // opposite of question - 
    public void flowWater(int[][]heights, int prevHeight, int currRow, int currCol,
    boolean[][] oceanVisited){
        // if indexOutOfBounds or already visited by ocean or the height is less than or equal,
        // dont flow from ocean to it. 
        // note the return condition is when height is less than or equal.
        // this is because 
        if(currRow < 0 || currCol < 0 || currRow >= rows || currCol >= cols
            || heights[currRow][currCol] < prevHeight || oceanVisited[currRow][currCol] 
        ){
            return;
        }
        // mark cell as visited by the ocean
        oceanVisited[currRow][currCol] = true;

        // attempt to flow water to all directions
        for(int[] d: directions){
            flowWater(heights,heights[currRow][currCol],
            currRow + d[0], currCol + d[1], 
            oceanVisited);
        }
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        rows = heights.length;
        cols = heights[0].length;
        boolean[][] pacificVisited= new boolean [rows][cols];
        boolean[][] atlanticVisited= new boolean [rows][cols];

        List<List<Integer>> output = new ArrayList<>();


        // flow from various oceans - horizontal border cells
        for(int c = 0; c < cols; c ++){
            flowWater(heights,Integer.MIN_VALUE,0, c, pacificVisited);
            flowWater(heights,Integer.MIN_VALUE,rows- 1, c, atlanticVisited);
        }
        // flow the vertical border cells
        for(int r=0; r < rows; r++){
            flowWater(heights,Integer.MIN_VALUE,r, 0, pacificVisited);
            flowWater(heights,Integer.MIN_VALUE,r, cols -1, atlanticVisited);
        }
        // now, return all cells which are in both oceans.
        for(int c = 0; c < cols; c ++){
            for(int r=0; r < rows; r++){

                if(pacificVisited[r][c] && atlanticVisited[r][c]){
                    output.add(Arrays.asList(r,c));
                }

            }
        }
        return output;
        
    }
}
