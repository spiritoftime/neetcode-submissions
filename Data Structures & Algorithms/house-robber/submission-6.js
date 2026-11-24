class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        for(let i =1; i < nums.length;i ++){
            if(i===1){
                nums[1] = Math.max(nums[0], nums[1])
                continue
            }
            nums[i] = Math.max(nums[i-1],nums[i]+nums[i-2])
        }
        return nums[nums.length-1]
    }
}
