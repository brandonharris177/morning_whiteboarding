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


