n = int(input())
cars_entering = list(map(int, input().split()))
cars_exiting = list(map(int, input().split()))

ref_map = {}
for i, car in enumerate(cars_exiting):
    ref_map[car] = i

def count_overtaking_cars(cars_entering):
    count_cars_to_fine = 0
    max_index = -1

    for car in cars_entering:
        if ref_map[car] > max_index:
            max_index = ref_map[car]
        else:
            count_cars_to_fine += 1
    return count_cars_to_fine

print(count_overtaking_cars(cars_entering))

        

