class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int bestf = 1;
        int bestb = 1;
        int streakf = 1;
        int streakb = 1;
        for (int i = 1; i < nums.size(); i++){
            if (nums[i] > nums[i - 1]){
                streakb = 1;
                streakf++;
                bestf = max(bestf, streakf);
            }
            else if (nums[i] < nums[i - 1]){
                streakf = 1;
                streakb++;
                bestb = max(bestb, streakb);
            }
            else{
                streakf = 1;
                streakb = 1;
            }
        }
        return max(bestf, bestb);

    }
};