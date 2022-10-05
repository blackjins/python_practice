'''
이전 문제의 `palindrome()` 함수가 문자열에 포함된 공백(space)을 무시하도록 
수정하라.
'''

# 아래 코드에서 pass 를 적절한 명령문으로, None 을 적절한 표현식으로 대체하라.

def palindrome(aString):
    reverse_aString = aString[::-1]
    noneWhitspace_reverse_aString = reverse_aString.replace(" ","")
    noneWhitspace_aString = aString.replace(" ","")
    if noneWhitspace_aString == noneWhitspace_reverse_aString:
        return "Success"
    else:
        return "Fail"

assert palindrome("race car") == "Success"
assert palindrome("tom ato") == "Fail"
assert palindrome("인싸의사의 싸인") == "Success"
assert palindrome("다시 합창합시다") == "Success"