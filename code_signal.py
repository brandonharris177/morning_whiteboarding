def checkPalindrome(inputString):
    reverse_string = ''
    for num in range(1, len(inputString)+1):
        print(inputString[-num])
        reverse_string = reverse_string + inputString[-num]
        
    if reverse_string == inputString:
        return True
    else:
        return False

checkPalindrome("abcdef")

