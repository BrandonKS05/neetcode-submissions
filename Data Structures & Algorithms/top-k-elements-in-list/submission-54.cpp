class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for(const auto& num: nums) freq[num]++;
        vector<pair<int, int>> newlist;
        for(const auto& [num, frequency]: freq){
            newlist.push_back({num, frequency});
        }
        auto f = [](const auto& a, const auto& b){
            return b.second < a.second;
            };
        sort(newlist.begin(), newlist.end(), f);

        vector<int> res;
        for (long long i = 0; i < k * 1LL; i++){
            res.push_back(newlist[i].first);
        }
        return res;
       
    }
};
