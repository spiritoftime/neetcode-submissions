class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let profit = 0
        let sell = prices[0]
        let buy = prices[0]
        for(const p of prices){
            if(buy > p){
                buy = p
                sell = p
            }
            sell = Math.max(sell, p)
            profit = Math.max(sell - buy, profit)
        }
        return profit
    }
}
