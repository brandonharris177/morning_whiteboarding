# def checkPalindrome(inputString):
#     reverse_string = ''
#     for num in range(1, len(inputString)+1):
#         print(inputString[-num])
#         reverse_string = reverse_string + inputString[-num]
        
#     if reverse_string == inputString:
#         return True
#     else:
#         return False

# checkPalindrome("abcdef")

# def almostIncreasingSequence(sequence):
#     if len(sequence) == 2:
#         return True

#     last_num = -1
#     almost_increasing = True
#     for num in range(0, len(sequence)-1):
#         if sequence[num] >= sequence[num+1]:
#             last_num = num-1
#             if num == 0 or sequence[num] == sequence[num+1]:
#                 print("this")
#                 sequence.pop(num)
#                 break
#             elif num+3 > len(sequence):
#                 if sequence[num+1] < sequence[num]:
#                     sequence.pop(num+1)
#                     break
#                 else:
#                     sequence.pop(num)
#                     break
#             elif sequence[num] < sequence[num+2] and sequence[num] > sequence[num-1]:
#                 print("this one")
#                 print(sequence[num+1])
#                 sequence.pop(num+1)
#                 print(sequence)
#                 break
#             else:
#                 sequence.pop(num)
#                 print(sequence)
#                 break
            
#     if last_num < 0:
#         last_num = 0
            
#     for new_num in range(last_num, len(sequence)-1):
#         if sequence[new_num] >= sequence[new_num+1]:
#             almost_increasing = False
#             break

#     print(almost_increasing)
#     return almost_increasing

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

# def matrixElementsSum(matrix):
#     haunted = set()
    
#     value = 0
#     story = 0
#     while story < len(matrix):

#         for num in range(0, len(matrix[story])):
#             if matrix[story][num] == 0:
#                 haunted.add(num)
        
        
#         for num in haunted:
#             matrix[story][num] = 0
            
#         for num in matrix[story]:
#             value = value + num
        
#         story += 1 
        
#     return value
    
