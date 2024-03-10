

def find_num_of_smaller(n,m,n_arr,m_arr):

    result = [0] * m
    for i in range(m):
        count = 0

        for j in range(n):
            if m_arr[i] > n_arr[j]:
                count += 1
            if m_arr[i] < n_arr[j]:
                break
        result[i] = count

    return result


n, m = map(int, input().split())

n_list = list(map(int, input().split()))
m_list = list(map(int, input().split()))

print(*find_num_of_smaller(n,m,n_list, m_list))
