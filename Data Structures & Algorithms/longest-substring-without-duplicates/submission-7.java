class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        int start = 0;
        HashMap<Character,Integer> hm = new HashMap<>();

        for (int i = 0; i < s.length(); i ++){
            char c = s.charAt(i);

            hm.put(c,hm.getOrDefault(c,0) + 1);
            // if already present slide window
            while(hm.get(c) > 1){
                hm.put(s.charAt(start), 
                hm.get(s.charAt(start)) -1);
                start += 1;
            }
            res = Math.max(res,i - start + 1);

        }
        return res;
    }
}
