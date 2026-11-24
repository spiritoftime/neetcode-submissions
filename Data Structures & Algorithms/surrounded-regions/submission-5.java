class Solution {
    public boolean shouldChange(char[][] board, int r, int c){
        if(r < 0 || c < 0 || r >= board.length || c >= board[0].length){
            return false;
        }
        if(board[r][c] == 'X'){
            return true;
        }

        // change 'O' to 'X' first to prevent infinite loop
        board[r][c] = 'X';

        boolean toChange =  shouldChange(board,r-1,c) && shouldChange(board,r+1,c)
        && shouldChange(board,r,c-1) && shouldChange(board,r,c + 1);

        board[r][c] = 'O';
        return toChange;
    }
    public void solve(char[][] board) {
        int row = board.length;
        int col = board[0].length;
        for (int r = 0; r < row; r++){
            for (int c = 0; c < col ; c++){
                if(board[r][c] == 'O'){
                    boolean toChange = shouldChange(board,r,c);
                    if(toChange){
                        board[r][c] = 'X';
                    } 
                }
            }
        }
    }
}
