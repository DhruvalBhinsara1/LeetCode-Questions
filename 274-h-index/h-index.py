class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()

        citations.reverse()

        h_index = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break
        return h_index