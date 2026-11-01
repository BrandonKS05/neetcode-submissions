class Solution {
    public boolean isMonotonic(int[] nums) {
        for(int i = 1; i < nums.length; i++){
            if (nums[i] < nums[i - 1]){
                for (int j = 1; j < nums.length; j++){
                    if (nums[j] > nums[j - 1]){
                        return false;
                    }
                }
                return true;
            }
            else if (nums[i] > nums[i - 1]){
                for (int k = 1; k < nums.length; k++){
                    if (nums[k] < nums[k - 1]){
                        return false;
                    }
                }
                return true;
            }
            else{
                continue;
            }
        }
        return true;
    }
}