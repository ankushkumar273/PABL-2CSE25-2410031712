import heapq

def kth_smallest(arr, k):
    return heapq.nsmallest(k, arr)[-1]


arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_smallest(arr, k))

