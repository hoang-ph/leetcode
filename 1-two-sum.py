class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hashmap to store the value that we already computed
        # store nums[i] as key and index as value
        numDict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numDict:
                return [i, numDict.get(diff)]
            numDict[nums[i]] = i
