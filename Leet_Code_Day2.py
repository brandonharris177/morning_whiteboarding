######Problem 1################
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        
        count = 0
        while count < len(nums)-1:
            for num in range(count+1, len(nums)):
                print(num)
                value = nums[count] + nums[num]
                table[value] = [count, num]
            count += 1

        return table[target]