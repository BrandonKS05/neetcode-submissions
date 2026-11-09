
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        unordered_map<int, int> freq;
        for(auto a: nums) freq[a]++;
        priority_queue<pair<int, int>> maxh;
        for(const auto& [num, f]: freq) maxh.push({f, num});
        while (k--){
            res.push_back(maxh.top().second);
            maxh.pop();
        }
        return res;

        
    }
};
