'''
'racecar', '토마토', 'stats'와 같이 앞뒤를 뒤집어도
똑같은 문자열을 (palindrome)이라고 한다. 
문자열이 주어질 때, 그 문자열이 회문이면 `Success` 를, 아니면 `Fail` 을 반환하는 함수
`palindrome()` 를 작성하여라.

힌트: 문자열 인덱싱, 슬라이싱 활용
'''
# 아래 코드에서 pass 를 적절한 명령문으로, None 을 적절한 표현식으로 대체하라.

def palindrome(aString):
    reverse_aString = aString[::-1]
    if aString == reverse_aString:
        return "Success"
    else:
        return "Fail"



assert palindrome("racecar") == "Success"
assert palindrome("tomato") == "Fail"
assert palindrome("기러기") == "Success"
assert palindrome("인싸 의사의 싸인") == "Success"
assert palindrome("다시 합창합시다") == "Fail"