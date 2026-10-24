class Solution {
public:
    int findgreater(int num, vector<int>& nums2){
        int idx = -1;
        for(int j = 0; j < nums2.size(); j++){
            if (nums2[j] == num){
                idx = j;
                }
            }
        for(int j = idx + 1; j < nums2.size(); j++){
            if (nums2[j] > num){
                return nums2[j];
                }
            }
            return -1;
        }
    vector<int> res;
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        for(int i = 0; i < nums1.size(); i ++){
            res.push_back(findgreater(nums1[i], nums2));
        }
        return res;
    }
};