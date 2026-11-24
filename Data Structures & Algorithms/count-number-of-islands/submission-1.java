class Solution {
    public void setWater(char[][] grid, int rowIndex, int colIndex){
        if(rowIndex < 0 || colIndex < 0 || colIndex >=  grid[0].length
        || rowIndex >=  grid.length
        
       || grid[rowIndex][colIndex] == '0'){
            return;
        }
        // set current to 0
        grid[rowIndex][colIndex] = '0';

        setWater(grid,rowIndex + 1, colIndex);
        setWater(grid,rowIndex - 1, colIndex);

        setWater(grid,rowIndex, colIndex-1);

        setWater(grid,rowIndex, colIndex+1);

    }
    public int numIslands(char[][] grid) {
        // go through every single island
        // attempt to convert every single island into water
        // if water dont do anything
        int numIslands = 0;
        for(int r = 0; r < grid.length; r++){
            for (int c = 0; c < grid[0].length; c ++){
                //  if it is an island, attempt to convert all adjacent islands to water
                if(grid[r][c] == '1'){
                    numIslands += 1;
                    setWater(grid,r,c);
                }
            }
        }
        return numIslands;
    }
}
