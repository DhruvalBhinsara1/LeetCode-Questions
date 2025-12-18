class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        total_sum = n * (n + 1) // 2

        array_sum = sum(nums)

        missing_number = total_sum - array_sum

        return missing_number
