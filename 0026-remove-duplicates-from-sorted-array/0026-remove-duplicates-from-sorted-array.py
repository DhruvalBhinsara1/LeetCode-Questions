class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        write_index = 1

        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index