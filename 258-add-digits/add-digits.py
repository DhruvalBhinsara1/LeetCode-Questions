class Solution:
    def addDigits(self, num: int) -> int:
        for i in range(len(str(num))):
            sum_digits = 0
            for digit in str(num):
                sum_digits += int(digit)
            num = sum_digits
        
        return sum_digits