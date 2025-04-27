import heapq
from typing import List


def min_cost_to_connect_cables(cables: List[int]) -> int:
    heapq.heapify(cables)
    total_cost: int = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost


cables = [4, 3, 2, 6]
print("Minimum total cost:", min_cost_to_connect_cables(cables))
