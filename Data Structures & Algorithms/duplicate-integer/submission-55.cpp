class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if (nums.size() == 0) return false;
        return set<int>(nums.begin(), nums.end()).size() != nums.size();
        
    }
};