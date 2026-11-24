class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums, target) {
        const res = []
        function backtrack(state, i, target,curr){
            if(curr === target){
                res.push([...state])
                return
            }
            if(curr > target) return
            for(let start = i; start < nums.length; start ++ ){
                backtrack([...state,nums[start]], start, target, curr + nums[start])
            }
        }
        backtrack([],0,target,0)
        return res
    }

}
