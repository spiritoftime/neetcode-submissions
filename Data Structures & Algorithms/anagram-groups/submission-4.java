class Solution {
    // how to create an extra method (helper function)
    public String sortedString(String s) {
        // convert a string to an array so that we can sort the characters
        char[] sArray = s.toCharArray();
        // sort in ascending order
        Arrays.sort(sArray );
        // return the sorted string
        // go through a for loop through sArray
        String returnS = "";
        for (char c : sArray){
            returnS += c;
        }
        return returnS;
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ls = new ArrayList<>();
        // method 1: use a hashmap - the key is the sorted word
        // and the value will be a list of strings, where the strings
        // are anagrams to each other.
        // we can just combine all the lists together!
        // sort the strings
        // create a method to sort a string, and return the string back
        // testing the method - this should return 'act'
        // System.out.println(sortedString(
        //     "cat"
        // ));

        // create the hashmap
        HashMap<String, List<String> > hm = new HashMap<>();
        for (String s : strs){
            String sortedS = sortedString(s);
            // is sortedS already in the hashmap?
            if(hm.containsKey(sortedS)){
               List<String> valueLs = hm.get(sortedS);
               valueLs.add(s);
                hm.put(sortedS, valueLs);
            } else{
                // sortedS not in hashmap,
                // we need to create the list first
                // then put it in the hashmap
                List<String> valueLs = new ArrayList<>();
                valueLs.add(s);
                hm.put(sortedS, valueLs);
            }
            
        }

        // return the ls properly
        for(List<String> anagramLs: hm.values()){
            System.out.println(anagramLs);
            ls.add(anagramLs);
        }

        return ls;
    }
}
