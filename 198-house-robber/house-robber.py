class Solution:
    def rob(self, nums: List[int]) -> int:

        prev_no = 0

        prev_yes = 0

        for num in nums:
            temp = prev_no
            prev_no = max(prev_no, prev_yes)
            prev_yes = num + temp
        result = max(prev_no, prev_yes)

        return result