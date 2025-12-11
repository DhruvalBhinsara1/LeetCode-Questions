class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                    next_greater[stack.pop()] = num
            stack.append(num)

        while stack:
                next_greater[stack.pop()] = -1

        return [next_greater[num] for num in nums1]

        nums1 = [3,1,2]

        nums2 = [1,3,4,2]

        print(nextGreaterElement(nums1, nums2))