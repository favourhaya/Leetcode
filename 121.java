class Solution {
    public int maxProfit(int[] prices) {
        int mx = 0;

        int l = 0;
        int r = 1;

        while (r < prices.length){
            if(prices[r] - prices[l] > mx){
                mx = prices[r] - prices[l];
            }

            if (prices[r] < prices[l]){
                l = r;
            }
            r ++;

        }
        return mx;
        
    }
}