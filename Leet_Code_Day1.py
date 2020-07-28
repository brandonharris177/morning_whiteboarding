# https://leetcode.com/problems/contains-duplicate/submissions/

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         numbers = {}
#         duplicates = False
#         for num in nums:
#             if num in numbers:
#                 duplicates = True
#             else:
#                 numbers[num] = num
#         return duplicates  

# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_str = ''
        second_str = ''
        while l1 != None:
            first_str = first_str + str(l1.val)
            l1 = l1.next
        while l2 != None:
            second_str = second_str + str(l2.val)
            l2 = l2.next
        first_str = ''.join(reversed(first_str))
        second_str = ''.join(reversed(second_str))
        
        total = str(int(first_str) + int(second_str))
        
        total_list = []
         
        for number in total:
            total_list.append(int(number))
            
        total_list.insert(0, None)

        print(total_list)
        
        new_list = ListNode(None)
        current_new = new_list

        while len(total_list) > 1:
                current_new.next = ListNode(total_list[-1])
                current_new = current_new.next
                total_list.pop()

        return new_list.next
            
            