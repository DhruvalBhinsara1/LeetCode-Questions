# 7. Reverse Integer

class Solution:

    def reverse(self, x: int) -> int:

        if x < 0:
            sign = -1
        else:
            sign = 1

        abs_str = str(abs(x))
        reversed_str = abs_str[::-1]
        reversed_int = sign * int(reversed_str)

        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0


        return reversed_int