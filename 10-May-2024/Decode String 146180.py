# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        decoded_str = ""
        count = 0
        
        for char in s:
            if char.isdigit():
                count = count * 10 + int(char)
            elif char == '[':
                stack.append((count, decoded_str))
                count = 0
                decoded_str = ""
            elif char == ']':
                prev_count, prev_str = stack.pop()
                decoded_str = prev_str + decoded_str * prev_count
            else:
                decoded_str += char
        
        return decoded_str

