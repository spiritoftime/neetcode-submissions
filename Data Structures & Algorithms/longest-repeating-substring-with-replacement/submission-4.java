class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character,Integer> wordFreq = new HashMap<>();
        int longestSubstring = 0;        
        int highestFrequency = 0;

        int start = 0;
        for(int end = 0; end < s.length(); end ++){

            // increment the frequency
            wordFreq.put(s.charAt(end), 
            wordFreq.getOrDefault(s.charAt(end), 0) + 1);

            // get the largest frequency
            highestFrequency = Math.max(wordFreq.get(s.charAt(end)), 
            highestFrequency);


            // the currSubstring length  will be sum of the values of wordFreq.
            // if currLength - k > largestFrequency, need to shrink the window.
            int currLength = end - start + 1;
            if(currLength - k > highestFrequency){
                // decrement the frequency of the character at the start
                //  to shrink the window
                wordFreq.put(s.charAt(start), wordFreq.getOrDefault(s.charAt(start), 0) -1);
                start += 1;

            }

            // compute length of longestSubstring
            longestSubstring = Math.max(longestSubstring, end - start +1);

        }
        return longestSubstring;
    }
}
