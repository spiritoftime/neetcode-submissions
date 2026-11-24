class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // convert from primitive array type to ArrayList
        ArrayList<Integer> numbers = new ArrayList<>();
        ArrayList<List<Integer>> out = new ArrayList<>();
        for(int n :nums){
            numbers.add(n);
        }
        // sort in ascending order
        Collections.sort(numbers);

        // loop through the array. numbers.size() - 2 because triplet
        for (int i = 0; i < numbers.size() - 2; i++){
            int l = i+1;
            int r = numbers.size() - 1;


            // skip duplicate for first pointer
            if(i > 0 && numbers.get(i) == numbers.get(i-1)){
                continue;
            }

            // there will be no negative numbers for l and r.
            if(numbers.get(i) > 0){
                break;
            }

            while (l<r){

                int total = numbers.get(l) 
                + numbers.get(r) + 
                numbers.get(i);
                
                // right pointer is largest number. shifting it leftward
                // decreases total.
                if(total > 0){
                    r -=1;
                }

                else if( total < 0){
                    l+=1;
                }

                else{

                    List<Integer> triplets = Arrays.asList(
                        numbers.get(l),
                        numbers.get(i),
                        numbers.get(r));
                    out.add(triplets);
                    
                    l++;
                    r--;
                    // skip duplicate values - increment the left pointer
                    while(l<r && numbers.get(l) == numbers.get(l-1)){
                        l += 1;
                    }


                }
            }
        }
        return out;
    }
}
