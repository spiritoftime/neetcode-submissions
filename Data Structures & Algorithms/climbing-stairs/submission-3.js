class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
    let first = 1
    let second = 1
    for (let i = 2; i <=n; i ++){
        const tmp = second
        second = first + second
        first = tmp
        
    }
    return second
    }
}

