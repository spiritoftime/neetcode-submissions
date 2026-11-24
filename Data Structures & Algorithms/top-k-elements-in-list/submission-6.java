class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> numFreq = new HashMap<>();
        HashMap<Integer,ArrayList<Integer>> freqNum = new HashMap<>();
        ArrayList<Integer> out = new ArrayList<>();

        // populate the numFreq first - num is key and freq is value
        for(int n : nums){
            numFreq.put(n, numFreq.getOrDefault(n,0) +1);
        }



        // populate FreqNum - freq is the key and num is the value.
        for(Map.Entry<Integer,Integer> e: numFreq.entrySet()){
            ArrayList<Integer> ls = 
            freqNum.getOrDefault(e.getValue(), new ArrayList<Integer>());

            // add the num into the ls
            ls.add(e.getKey());
            // update the value
            freqNum.put(e.getValue(),ls);
        }
        System.out.println(freqNum.toString());
        for(int i = nums.length; i >=0; i-- ){
            if(freqNum.containsKey(i)){

                // get the value out of freqNum which is the number
                ArrayList<Integer> numbers = freqNum.get(i);
                for(int n: numbers){
                    out.add(n);
                    if(out.size() == k){
                            break;
                        }
                }
                if(out.size() == k){
                    break;
                }
            }
        }
        // convert arrayList to integer array
        int[] arr = new int [out.size()];
        for(int i = 0; i < arr.length; i ++){
            arr[i] = out.get(i);
        }
        return arr;
    }
}
