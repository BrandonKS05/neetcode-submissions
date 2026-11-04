class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> res;
        std::unordered_map<int, int> seen;
        for (int i = 0; i <nums.size(); i++){
            int need = target - nums[i];
            if(seen.contains(need)){
                res.push_back(seen[need]);
                res.push_back(i);
                return res;
            }
            seen[nums[i]] = i;
            
        }
        res.push_back(1);
        return res;
              
        
    }
};
