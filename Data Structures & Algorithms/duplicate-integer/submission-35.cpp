class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> seen;
        for(auto num : nums){
            if(seen.count(num)){
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};