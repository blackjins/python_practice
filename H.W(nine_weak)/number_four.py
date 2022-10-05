'''
회문(palindrome) 판별기 `is_pal()` 을 재귀 함수로 구현하라.
회문은 읽는 순서를 뒤집어도 동일한 문장을 가리킨다.

* 기러기
* 탄도유도탄
* radar
* rotator
* level

단, 공백, 쉼표, 생략 기호, 마침표, 느낌표, 하이픈 등은 무시되며, 영어 알파벳의 대소문자도 구분하지 않는다. 즉 아래 문장들도 회문으로 인정받아야 한다.

* 다시 합창합시다.
* 야, 이 달은 밝은 달이야.
* Madam, I'm Adam.
* A man, a plan, a canal - Panama!
'''
def is_pal(s):
    assert isinstance(s, str) and len(s) > 1
    if s.isalnum:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
    if s[0] != s[-1]:
        return False
    elif s[0] == s[-1] and len(s) == 3:
        return True
    return is_pal(s[1:-1])


assert is_pal('기러기') == True
assert is_pal('다시 합창합시다.') == True
assert is_pal('radar') == True
assert is_pal('A man, a plan, a canal - Panama!') == True
assert is_pal('다시 합창') == False
assert is_pal('lovel') == False