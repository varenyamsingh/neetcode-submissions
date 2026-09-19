class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]

        return sum(
            min(tickets[i], target - (i > k))
            for i in range(len(tickets))
        )