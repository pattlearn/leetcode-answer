class Solution(object):
    def twoSum(self, nums, target):
        check = {}
        
        for idx in range(len(nums)):
            num = nums[idx]
            complement = target - num
            if num in check:
                return [check[num], idx]
            else:
                check[complement] = idx
        
        return 1