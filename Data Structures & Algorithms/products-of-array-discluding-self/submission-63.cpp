#include <iostream>
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::vector<int> left;
        int l = nums.size() - 1;
        int forward = 1;
        for(int n: nums){
            left.push_back(forward);
            forward = forward * n;
        }
        int backward = 1;
        while (l > -1){
            left[l] = left[l] * backward;
            backward = backward * nums[l];
            l -= 1;
        }
        return left;
    }
};
