
def isPalindrome(st):
    if len(st) <= 1: p = True
    else:
        if st[0] != st[-1]: p = False
        else: p = isPalindrome(st[1:-1])
    return p

def checkPalindrome(st):
    stu = st.upper()
    stu = stu.replace(' ','')
    print(st)
    palin = isPalindrome(stu)
    if palin == True: print('is a palindrome.')
    else: print('is not a palindrome.')
    print()

checkPalindrome('level')
checkPalindrome('noon')
checkPalindrome('rainbow')
checkPalindrome('no lemon no melon')
checkPalindrome('Step on no pets')
checkPalindrome('123454321')
checkPalindrome('borrow or rob')
checkPalindrome('12345321')