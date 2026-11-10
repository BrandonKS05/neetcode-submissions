typedef unordered_map<int, int> hashmap;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        hashmap hash;
        for(uint32_t i = 0; i < nums.size(); i++){
            long long need = (target - nums[i]) * 1LL;
            if (hash.contains(need)) return vector<int>{(int)hash[need], (int)i};
            hash[nums[i]] = i;
        }
        return vector<int>{-1, -1};
       
       
    }
};
