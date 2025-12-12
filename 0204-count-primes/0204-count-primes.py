class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        my_numb = [True] * n
        my_numb[0] = my_numb[1] = False

        p = 2
        while p * p < n:
            if my_numb[p]:
                for i in range(p*p, n, p):
                    my_numb[i] = False
            p += 1

        return sum(my_numb)
