class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    
        

        my_list = s.split()

        return len(my_list[-1])
        