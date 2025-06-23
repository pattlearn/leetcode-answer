class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        list_out = []
        nums = sorted(nums)
        
        for i in range(len(nums) - 2):
            if (nums[i] == nums[i-1]) and i != 0:
                continue
            
            l = i + 1
            r = len(nums) - 1
            if nums[i] > 0:
                break
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                if current_sum == 0:
                    list_out.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r-= 1

                if current_sum < 0:
                    l += 1
                elif current_sum > 0:
                    r -= 1
        
        return list_out