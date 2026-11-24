class Solution {
    public boolean isValid(String s) {

        // if bracket is closing bracket, you need to pop
        // the top of the stack.
        // after you popped the stack, check that the popped
        // character is the same as the corresponding opening bracket
        // from the closing bracket.
        // if it is not it is an invalid string.

        ArrayList<Character> stack = new ArrayList<>();
        HashMap<Character,Character> closeOpen = new HashMap<>();

        // populate the hashmap with the correct brackets
        closeOpen.put('}','{');
        closeOpen.put(')','(');

        closeOpen.put(']','[');


        for (char c : s.toCharArray()){
        
            //  it is a opening bracket - append to the stack.
            if(!closeOpen.containsKey(c)){

                stack.add(c);
             } else{
                //  it is a closing bracket
                char correctOpen = closeOpen.get(c);

                
                //  there is no corresponding open bracket to even
                //  check
                if (stack.size() == 0){
                    return false;
                }
                // remove the most immediate character
                char topOfStack = stack.remove(stack.size() - 1);

                if(correctOpen != topOfStack){
                    return false;
                }
             }


        }

    if(stack.size() == 0){
        return true;
    } 
    return false;
    }
}
