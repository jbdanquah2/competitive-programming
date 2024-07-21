# Problem: D - Playlist - https://codeforces.com/gym/536373/problem/D

import heapq

def main(n, k, songs) -> int:

    songs.sort(key=lambda x: x[1], reverse=True)
    
    current_total_length = 0
    max_pleasure = 0
    min_heap = []
    
    for length, beauty in songs:
        # Add the current song's length to the total length
        current_total_length += length
        heapq.heappush(min_heap, length)
        
        # If we have more than k songs, remove the smallest length song
        if len(min_heap) > k:
            current_total_length -= heapq.heappop(min_heap)
        
        # Calculate the pleasure
        max_pleasure = max(max_pleasure, current_total_length * beauty)
    
    return max_pleasure

n, k = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]

print(main(n, k, songs))
