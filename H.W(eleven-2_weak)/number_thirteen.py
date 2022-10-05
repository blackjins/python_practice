'''
주어진 정수를 오름차순으로 정렬하여, 리스트 형태로 반환하는 `int2sorted_list()` 함수를 작성하라.
단, 양의 정수만 입력값으로 사용한다.
'''
# pass 와  None을 적절한 명령문과 표현식으로 대체하라.

def int2sorted_list(an_int):
    assert an_int > 0
    an_int = str(an_int)
    an_int = list(an_int)
    an_int = list(map(int, an_int))
    an_int = sorted(an_int)   
    an_int = list(map(str, an_int))
    return an_int

assert int2sorted_list(32145) == ['1', '2', '3', '4', '5']
assert int2sorted_list(435) == ['3', '4', '5']
