# Problem: Pow(x, n) - https://leetcode.com/problems/powx-n/

def myPow(self, x: float, n: int) -> float:

        # result = 1

        # if n == 0:
        #     return result

        # for i in range(0, abs(n)):

        #     if n >= 0:
        #         result *= x
        #     else:
        #         result /= x

        # return result

        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, (n - 1) // 2)
