"""
You are given n points on the straight line — the positions (x-coordinates) of the cities and m points on the same line — the positions (x-coordinates) of the cellular towers. All towers work in the same way — they provide cellular network for all cities, which are located at the distance which is no more than r from this tower.

Your task is to find minimal r that each city has been provided by cellular network, i.e. for each city there is at least one cellular tower at the distance which is no more than r.

If r = 0 then a tower provides cellular network only for the point where it is located. One tower can provide cellular network for any number of cities, but all these cities must be at the distance which is no more than r from this tower.

Input
The first line contains two positive integers n and m (1 ≤ n, m ≤ 105) — the number of cities and the number of cellular towers.

The second line contains a sequence of n integers a1, a2, ..., an ( - 109 ≤ ai ≤ 109) — the coordinates of cities. It is allowed that there are any number of cities in the same point. All coordinates ai are given in non-decreasing order.

The third line contains a sequence of m integers b1, b2, ..., bm ( - 109 ≤ bj ≤ 109) — the coordinates of cellular towers. It is allowed that there are any number of towers in the same point. All coordinates bj are given in non-decreasing order.

Output
Print minimal r so that each city will be covered by cellular network.

Examples
input
3 2
-2 2 4
-3 0
output
4
inputCopy
5 3
1 5 10 14 17
4 11 15
output
3

"""


def cellular_network(n, m, cities, towers):

    max_distance = 0
    for city in cities:
        min_distance = float('inf')
        for tower in towers:
            min_distance = min(min_distance, abs(city - tower))
        max_distance = max(max_distance, min_distance)
    return max_distance


n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))

res = cellular_network(n, m, cities, towers)
print(res)