class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        major = 0

        for num in nums:
            if count == 0:
                major = num
            count += (1 if num == major else -1)

        return major