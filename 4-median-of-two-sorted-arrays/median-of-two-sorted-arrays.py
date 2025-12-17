class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)

        nums1.sort()

        arr_len = len(nums1)

        if arr_len % 2==0:
            mid_element = (nums1[arr_len//2-1]+nums1[arr_len//2])/2
        else:
            mid_element = nums1[arr_len//2]
        
        return mid_element