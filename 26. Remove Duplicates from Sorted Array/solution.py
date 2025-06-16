class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        dummy = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                dummy.append(nums[i])
                k += 1
                
        nums[:] = dummy
                  
        return k