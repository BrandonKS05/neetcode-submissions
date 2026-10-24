class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::vector<int> res(k);
        std::unordered_map<int, int> hashmap;
        for(int num: nums){
            if(!hashmap.contains(num)){
                hashmap[num] = 0;
            }
            hashmap[num] += 1;
        }
        std::vector<std::pair<int, int>> freq(hashmap.begin(), hashmap.end());
        std::sort(freq.begin(), freq.end(), [](auto& a, auto& b){return a.second > b.second;});
        std::transform(freq.begin(), freq.begin() + k, res.begin(), [](auto& a){return a.first;});
        return res;
    }
};
