class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write_index = 0

        for num in nums:
            if write_index < 2 or num != nums[write_index - 2]:
                nums[write_index] = num
                write_index += 1

        return write_index