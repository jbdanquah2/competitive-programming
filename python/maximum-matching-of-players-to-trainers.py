from collections import defaultdict


def max_matching_players_trainers(players: list, trainers: list):

    count = 0
    j = 0
    for i in range(len(players)):
        while j < len(trainers):
            if players[i] <= trainers[j]:
                count += 1
                j += 1
                break
            j += 1

    return count


print(max_matching_players_trainers([1,1,1],[10]))


