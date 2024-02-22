"""

Mishka has got n empty boxes. For every i (1 ≤ i ≤ n), i-th box is a cube with side length ai.

Mishka can put a box i into another box j if the following conditions are met:

i-th box is not put into another box;
j-th box doesn't contain any other boxes;
box i is smaller than box j (ai < aj).
Mishka can put boxes into each other an arbitrary number of times. He wants to minimize the number of visible boxes. A box is called visible iff it is not put into some another box.

Help Mishka to determine the minimum possible number of visible boxes!

Input
The first line contains one integer n (1 ≤ n ≤ 5000) — the number of boxes Mishka has got.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 109), where ai is the side length of i-th box.

Output
Print the minimum possible number of visible boxes.

"""

num_of_boxes = int(input())
boxes = list(map(int, input().split(' ')))
boxes.sort()

for i in range(1, len(boxes)):
    if boxes[i] > boxes[i-1]:
        num_of_boxes -= 1


print(num_of_boxes)



