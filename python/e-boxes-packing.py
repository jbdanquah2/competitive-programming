# how do implement this using hashpmap or a dict:
# create a dict to store the boxes and their count
# iterate through the boxes and store the boxes in the dict
# iterate through the dict and compare the boxes to get the minimum number of visible boxes
# return the minimum number of visible boxes

def e_boxes_packing():
    n = int(input())
    boxes = list(map(int, input().split()))
    box_dict = {}

    for box in boxes:
        if box in box_dict:
            box_dict[box] += 1
        else:
            box_dict[box] = 1

    max_box = 0

    for box in box_dict:
        if box_dict[box] > max_box:
            max_box = box_dict[box]

    print(max_box)

e_boxes_packing()

# Time complexity: O(n)
# Space complexity: O(n)



