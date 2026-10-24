#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        
        int* newpoop = new int[2 * n];  // allocate 2n
        
        for (int i = 0; i < n; i++) {
            newpoop[i] = nums[i];
            newpoop[i + n] = nums[i];
        }

        vector<int> ans(newpoop, newpoop + 2 * n); // copy into vector
        delete[] newpoop; // free memory
        
        return ans;
    }
};