class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longestLength = 0;
        int start = 0;
        // initialize the hashset with wrapper class Character
        // not the primitive data type. Generics use wrapper classes
        HashSet<Character> uniqueChars = new HashSet<>();
        for (char c: s.toCharArray()){

            while (uniqueChars.contains(c)){

                uniqueChars.remove(s.charAt(start));
                start += 1;

            }

            // add the current character into the hashset
            uniqueChars.add(c);
            longestLength = Math.max(longestLength, uniqueChars.size());

        }

        return longestLength;
    }
}
