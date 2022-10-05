'''
정수 `a`와 자연수 `n`을 입력받아, `n`개의 항목을 갖는 리스트를 출력하는 
`int_clone()` 함수를 작성하여라.
단, 리스트의 항목은 `a`부터 시작하고, 그 다음 항목은 이전 항목보다 `a`만큼 크다.        
'''
# pass 와  None을 적절한 명령문과 표현식으로 대체하라.

def int_clone(a, n):
    assert n > 0
    tmp = a
    num = []
    for i in range(n):
        num.append(a)
        a = a + tmp
    
    return num
assert int_clone(3, 4) == [3, 6, 9, 12]
assert int_clone(2, 3) == [2, 4, 6]