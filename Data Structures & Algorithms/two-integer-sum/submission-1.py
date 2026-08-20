class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] ==  target:
        #             return [i, j]

        hashmap = {}
        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in hashmap:
                return [hashmap[needed], i]
            hashmap[nums[i]] = i
