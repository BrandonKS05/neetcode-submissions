class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++){
            if (i > 0 && nums[i - 1] == nums[i]){
                continue;
            }

            long long l = i + 1;
            long long  r = nums.size() - 1;

            while (l < r){
                long long total = nums[i] + nums[l] + nums[r];
                if (total == 0){
                    res.push_back({nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]){
                        l++;
                    }
                    while (r > l && nums[r] == nums[r + 1]){
                        r--;
                    }
                  
                }
                else if (total < 0){
                        l++;
                } else{
                    r--;
                }
            }

        }
        return res;
    }
};
