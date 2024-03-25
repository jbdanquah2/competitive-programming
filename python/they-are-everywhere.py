

def minimum_num_flat(n: int, s: str):

    left = 0
    right = 0
    s_set = set()
    count_room = 0

    while right < n:
        if s[right] not in s_set:
            s_set.add(s[right])
            right += 1
            count_room = max(count_room, right - left)
        else:
            if right - 1 == 0:
                left -= 1
            left += 1
            right += 1

    return count_room


n = int(input())
s = input()
print(minimum_num_flat(n, s))

