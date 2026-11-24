class Solution {
    public int maxProfit(int[] prices) {
        // set buy and sell as first day.
        // the moment you find a lower price, sell 
        // what you have then set buy and sell to the lower price.
        // else do nothing and just hold.

        int profit = 0;
        int buy = 0;

        for (int sell = 1; sell < prices.length; sell ++){

            if(prices[sell] < prices[buy]){
                buy = sell;
            } else{
                // check profit daily
                profit = Math.max(prices[sell] - prices[buy], profit);
            }
            
        }



        return profit;
    }
}
