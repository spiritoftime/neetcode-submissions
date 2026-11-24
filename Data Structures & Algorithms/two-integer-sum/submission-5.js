class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const hm = {}
        for(let i = 0 ; i < nums.length; i ++){
            const n = nums[i]
            if(n in hm){
                return [hm[n], i]
            }else{
                hm[target - n] = i
            }
        }

    }
}
