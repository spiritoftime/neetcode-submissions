class Solution {
    private static int numWays = 0;
    
    private HashSet<Character> zeroToNine = new HashSet<>(Arrays.asList('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'));
    private HashSet<Character> zeroToSix = new HashSet<>(Arrays.asList('0', '1', '2', '3', '4', '5', '6'));

    private int dfs(int idx, HashMap<Integer, Integer> memo, String s) {
        if (idx == s.length()) {
            return 1; // reached the end of the string
        }

        // Check if the result is already computed
        if (memo.containsKey(idx)) {
            return memo.get(idx);
        }

        int num = 0;

        // Leading zero - unable to decode
        if (s.charAt(idx) == '0') {
            return 0;
        }

        // Try to decode the next letter (single character)
        num += dfs(idx + 1, memo, s);

        // Try to decode two characters at the same time
        if (idx < s.length() - 1) {
            char first = s.charAt(idx);
            char second = s.charAt(idx + 1);
            if ((first == '1' && zeroToNine.contains(second)) || (first == '2' && zeroToSix.contains(second))) {
                num += dfs(idx + 2, memo, s);
            }
        }

        // Memoize the result
        memo.put(idx, num);

        return num;
    }

    public int numDecodings(String s) {
        HashMap<Integer, Integer> memo = new HashMap<>();
        return dfs(0, memo, s);
    }
}
