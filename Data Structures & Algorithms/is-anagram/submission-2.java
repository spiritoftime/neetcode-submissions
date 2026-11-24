class Solution {
    public void populateHm(HashMap<Character, Integer> sFreq, String s){
        for (char c: s.toCharArray()){
            sFreq.put(c,sFreq.getOrDefault(c,0) +1);
        }
    }

    public boolean isAnagram(String s, String t) {
        // check 1 - must be of same length
        if(s.length() != t.length()){
            return false;
        }
        HashMap<Character, Integer> sFreq = new HashMap<>(); 
        HashMap<Character, Integer> tFreq = new HashMap<>(); 
        populateHm(sFreq,s);
        populateHm(tFreq,t);
        //  check through every key value entry
        for(Map.Entry<Character,Integer> e: sFreq.entrySet()){
            char key = e.getKey();
            int value = e.getValue();
            // use getOrDefault so wont error
            if(value != tFreq.getOrDefault(key,0)){
                return false;
            }
        }
        return true;

    }
}
