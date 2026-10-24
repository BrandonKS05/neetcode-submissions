class Solution:
    def twoSum_return_next_i_j_for_i_in_range_len_nums_for_j_in_range_i_plus_1_len_nums_if_nums_i_plus_nums_j_equals_target(self, nums, target):
        return next([i, j] for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i]+nums[j] == target)

    twoSum = twoSum_return_next_i_j_for_i_in_range_len_nums_for_j_in_range_i_plus_1_len_nums_if_nums_i_plus_nums_j_equals_target