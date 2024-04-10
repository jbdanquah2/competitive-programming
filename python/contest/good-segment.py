

def longest_good_segement(length: int, string: str):

    left = 0
    right = 0
    count = 0

    if length == 1:
        print(1)
        return

    while right < n - 1:

        while ord(s[right]) + 1 == ord(s[right + 1]):
            right += 1
            if right == n - 1:
                break
        count = max(count, right - left + 1)
        left = right + 1
        right += 1

    print(count)


n = int(input())
s = input()
longest_good_segement(n, s)
