class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total_len = (len(nums1) + len(nums2))
        pos = total_len / 2
        if total_len % 2 == 0:
            is_odd = False
        else:
            is_odd = True
        
        count = 0
        pointer1 = 0
        pointer2 = 0
        merge_list = []
        
        while (pointer1 < len(nums1)) or (pointer2 < len(nums2)):
            if pointer1 >= len(nums1):
                num1 = float("inf")
            else:
                num1 = nums1[pointer1]
            if pointer2 >= len(nums2):
                num2 = float("inf")
            else:
                num2 = nums2[pointer2]
            
            if num1 <= num2:
                count += 1
                pointer1 += 1
                merge_list.append(num1)
            else:
                count += 1
                pointer2 += 1
                merge_list.append(num2)
            if count > pos:
                if is_odd:
                    return float(merge_list[-1])
                else:
                    return float((merge_list[-1] + merge_list[-2])/2)