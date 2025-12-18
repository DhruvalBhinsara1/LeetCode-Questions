class Solution:
    def reverseWords(self, s: str) -> str:
        
        my_list = s.split()

        my_list.reverse()

        s = " ".join(my_list)
        
        return s