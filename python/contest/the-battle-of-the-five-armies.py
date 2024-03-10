

def cal_power_level():
    a, b, c, d, e = map(int, input().split())
    m, n, o, p, q = map(int, input().split())

    army_one = a * m + b * n + c * o
    army_two = d * p + e * q

    if army_one > army_two:
        print("WIN")

    elif army_one < army_two:
        print("LOSE")

    else:
        print("DRAW")


cal_power_level()

