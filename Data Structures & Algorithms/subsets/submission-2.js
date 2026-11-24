class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */

    subsets(nums) {
        function backtrack(nums,state,i,res){
            res.push([...state])

            for(let j = i; j < nums.length; j ++){

                state.push(nums[j])
                backtrack(nums,state,j+1,res)
                state.pop(nums[j])
            }
        }
        const res = []
        backtrack(nums,[],0,res)
        return res
    }
}
