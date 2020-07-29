# def remove_kth_from_end(head, k):
#     linked_list = []
    
#     current_node = head
#     while current_node != None:
#         linked_list.append(current_node)
#         current_node = current_node.next
        
#     if k > len(linked_list):
#         return head
    
#     if k != 0:    
#         linked_list.pop(-k)
        
#     new_list = ListNode(None)
#     current_new = new_list
    
#     pointer = 0
#     while pointer < len(linked_list):
#         print(linked_list[pointer].value)
#         current_new.next = ListNode(linked_list[pointer].value)
#         current_new = current_new.next
#         pointer += 1
    
#     return new_list.next


# def first_not_repeating_character(s):
#     hash_table = {}
    
#     for num in range(0, len(s)):
#         if s[num] in hash_table:
#             hash_table[s[num]].append(num)
#         else:
#             hash_table[s[num]] = []
#             hash_table[s[num]].append(num)
            
#     first_occorance = len(s)
#     letter = "_"
    
#     print(hash_table)
    
#     for key, item in hash_table.items():
#         if len(item) == 1 and item[0] <= first_occorance:
#             first_occorance = item[0]
#             print(key, item[0])
#             letter = key
            
#     return letter

# def uncover_spy(n, trust):
#     hash_table = {}
    
#     innocents = set()
    
#     spy = -1
    
#     for pair in trust:
#         if pair[1] in hash_table:
#             hash_table[pair[1]] += 1
#         else:
#             hash_table[pair[1]] = 1
#             innocents.add(pair[0])
            
#     for key, value in hash_table.items():
#         if value == n-1 and key not in innocents:
#             spy = key
#             break
            
#     return spy