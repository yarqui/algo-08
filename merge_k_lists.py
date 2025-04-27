from typing import List
import heapq


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    h = list(heapq.merge(*lists))
    return h


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_lists = merge_k_lists(lists)
print("merged_lists:", merged_lists)
