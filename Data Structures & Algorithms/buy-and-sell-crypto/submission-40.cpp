using ll = long long;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int best = 0;
        ll cand = 0;
        for (ll i = 1; i < prices.size(); i++){
            if (prices[i] < prices[cand]){
                cand = i;
            }
           
            best = max(best, prices[i] - prices[cand]);
        }

    return best;
    }
};
