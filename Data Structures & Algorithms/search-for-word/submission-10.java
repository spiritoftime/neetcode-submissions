class Solution {
    private boolean exists = false;
    

    // ISSUE: if you use 2 hashsets, you are not properly checking for a 
    // visited coordinate. eg: visited row 3, row 2, col 1,4.
    // you do not know if it is (3,1) or (2,1) is visited.
    public void checkForWord(char[][] board, 
    String word, 
    HashSet<Integer> visitedIndiciesEncrypted,
    String currentWord, int currentRowIndex, int currentColIndex ){
        // if the instance variable exists is already true,
        // auto terminate. the word has long been found, no need
        // to continue to iterate.
        if(this.exists == true){
            return;
        }

        // is the current row and col index even valid? if not, exit
        if(currentRowIndex >= board.length || currentRowIndex <0
        || currentColIndex >= board[0].length ||  currentColIndex < 0   ){
            return;
        }
        // calculate one unique integer key using the row and column 
        // so that the visitedIndiciesEncrypted can function properly
        // as a unique coordinate checker

        int uniqueIntegerKey = currentRowIndex * board[0].length + currentColIndex;
        
        // is the uniqueIntegerKey present in the visitedIndiciesEncrypted 
        // hashset? if it is exit
        if(visitedIndiciesEncrypted.contains(uniqueIntegerKey)){
            return;
        }
        // now, we can try to construct the word and then check.
        currentWord += board[currentRowIndex][currentColIndex];
        // when length exceeds, terminate
        if(currentWord.length() > word.length()){
            return;
        }
        // is the currentWord same as the word? if yes, return true.
        // take note that for string comparison, we use the .equals()
        // dont just do ==. if interested read more about references.
        if(currentWord.equals(word)){
            this.exists = true;
            return;
        }
        // add the current coordinate as visited
        visitedIndiciesEncrypted.add(uniqueIntegerKey);

        // explore all possible neigbouring cells
        // there are 4 possible areas -> up down left and right
        checkForWord(board,word,visitedIndiciesEncrypted,currentWord,
        currentRowIndex,currentColIndex + 1 );
        checkForWord(board,word,visitedIndiciesEncrypted,currentWord,
        currentRowIndex,currentColIndex - 1 );
        checkForWord(board,word,visitedIndiciesEncrypted,currentWord,
        currentRowIndex + 1,currentColIndex);
        checkForWord(board,word,visitedIndiciesEncrypted,currentWord,
        currentRowIndex - 1,currentColIndex);


        // as per backtracking, always restore the state.
        // in this case, the state is the visitedIndiciesEncrypted hashset.
        visitedIndiciesEncrypted.remove(uniqueIntegerKey);
        // no need for this, because when you += a string it 
        // already initializes a new string variable
        // remove the character from the currentWord
        // currentWord = currentWord.substring(0,currentWord.length() -1);
    }
    
    public boolean exist(char[][] board, String word) {
        // boundary: IndexOutOfBounds
        //  it shouldnt be allowed to go back to where it visited
        //  finally, it is possible that the word may start with a different
        // letter. hence all combinations for each letter must be checked.
        // when the currentWord length exceeds word length, terminate exploration
        HashSet<Integer> visitedIndiciesEncrypted = new HashSet<>();
        String currentWord = "";

// for every character, call checkForWord.
for(int currentRowIndex = 0; currentRowIndex < board.length; currentRowIndex++ ){
    for (int currentColIndex = 0; currentColIndex < board[0].length; currentColIndex ++){
        
        checkForWord(board, 
    word, 
    visitedIndiciesEncrypted,
    currentWord,currentRowIndex,currentColIndex );
}
    if(this.exists) return true;
    }
            return this.exists;

}
}