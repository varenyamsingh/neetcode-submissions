class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))

        # another sol
        seen = set()
        for x in nums:
            if x in seen:
                return True

            seen.add(x)

        return False
