class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []

        for i in range(len(pairs)):
            current = pairs[i]
            j = i - 1

            while j >= 0 and pairs[j].key > current.key:
                pairs[j + 1] = pairs[j]
                j -= 1

            pairs[j + 1] = current
            result.append(pairs.copy())

        return result