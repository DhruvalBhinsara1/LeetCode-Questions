class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total_apples = sum(apple)
        for i, cap in enumerate(capacity, 1):
            total_apples -= cap
            if total_apples <= 0:
                return i
        return len(capacity)
