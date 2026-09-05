class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr = 0
        total = 0

        for arrival, cook in customers:
            curr = max(curr, arrival) + cook
            total += curr - arrival

        return total / len(customers)