class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const hm = {}
        for(let i = 0; i < nums.length; i ++){
            if(nums[i] in hm){
                return [hm[nums[i]], i]
            }
            else{
                hm[target-nums[i]] = i
            }
        }
    }
}
