class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        nums.sort((a,b)=>a-b)
        const res = []
        for(let i = 0; i < nums.length; i ++){
            if(i > 0 && nums[i] === nums[i-1]) continue
            let l = i+1
            let r = nums.length - 1
            while (l < r){
                const total = nums[l] + nums[i] + nums[r] 
                if(total === 0) {
                    res.push( [ nums[l], nums[i], nums[r] ] )
                    l += 1
                    r-=1
                    while(l < r && nums[l] === nums[l-1]) l+=1

                }
                if(total < 0) {
                    l +=1
                }
                if(total >0) {
                     r-=1
                }   
            }
        }
        return res
    }
}
