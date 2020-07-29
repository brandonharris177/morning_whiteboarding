######Problem 1################
# https://leetcode.com/problems/two-sum/

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         table = {}
        
#         count = 0
#         while count < len(nums)-1:
#             for num in range(count+1, len(nums)):
#                 print(num)
#                 value = nums[count] + nums[num]
#                 table[value] = [count, num]
#             count += 1

#         return table[target]


#######################Problem 2##############################
#https://leetcode.com/problems/implement-queue-using-stacks/

# class MyQueue:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.queue = []
        

#     def push(self, x: int) -> None:
#         """
#         Push element x to the back of queue.
#         """
#         self.queue.append(x)
        

#     def pop(self) -> int:
#         """
#         Removes the element from in front of queue and returns that element.
#         """
#         value = self.queue.pop(0)
#         return value
        

#     def peek(self) -> int:
#         """
#         Get the front element.
#         """
#         return self.queue[0]
        

#     def empty(self) -> bool:
#         """
#         Returns whether the queue is empty.
#         """
#         if len(self.queue) == 0:
#             return True
#         else:
#             return False


#####################Problem 3###################
# https://leetcode.com/problems/group-anagrams/

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hash_table = {}
        
#         for word in strs:
#             key = ''.join(sorted(word))
#             if key in hash_table:
#                 hash_table[key].append(word)
#             else:
#                 hash_table[key] = []
#                 hash_table[key].append(word)
        
#         anagrams = []
                
#         for key, value in hash_table.items():
# 	        anagrams.append(value)
        
#         return anagrams