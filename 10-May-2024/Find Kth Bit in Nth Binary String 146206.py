# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def generateSn(n):
            if n == 1:
                return "0"
            else:
                prev = generateSn(n - 1)
                inverted_prev = "".join('1' if bit == '0' else '0' for bit in prev)
                return prev + "1" + inverted_prev[::-1]

        Sn = generateSn(n)
        return Sn[k - 1]
        