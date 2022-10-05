'''
튜플이 인자로 들어오면 튜플의 기존 항목들이 역순으로 추가된 튜플을 반환하는 
`tuple_double_rev()` 함수를 구현하라.
'''
# pass 와  None을 적절한 명령문과 표현식으로 대체하라.

def tuple_double_rev(t):
    tmp = t[::-1]


    return t + tmp
assert tuple_double_rev((1, 2, 3)) == (1, 2, 3, 3, 2, 1)
assert tuple_double_rev(('a', 'b')) == ('a', 'b', 'b', 'a')
