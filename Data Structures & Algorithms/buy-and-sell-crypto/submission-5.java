class Solution {
    public int maxProfit(int[] prices) {
        // set buy and sell as first day.
        // the moment you find a lower price, sell 
        // what you have then set buy and sell to the lower price.
        // else do nothing and just hold.

        int profit = 0;
        int buy = 0;
        int sell = 0;

        for (int i = 1; i < prices.length; i ++){
            // check profit everyday
            profit = Math.max(prices[sell] - prices[buy], profit);

            if(prices[i] < prices[buy]){
                buy = i;
            }
            sell = i;
        }
        // if highest price is at last day
        profit = Math.max(prices[sell] - prices[buy], profit);


        return profit;
    }
}
