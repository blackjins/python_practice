'''
양의 정수를 이진법으로 변환하는 `to_bin()` 회귀 함수를 구현하라.
단, 반환값은 이진법으로 작성된 문자열이어야 한다.
'''
i = 0
result = []
def to_bin(n):
    assert isinstance(n, int) and n > 0
    global i
    global result
    if i == 0:
        result = []
    a, b = divmod(n, 2)
    result.append(str(b))
    i = i + 1
    if a == 0:
        i = 0
        return "".join(result[::-1]) 
    else:
        return to_bin(a)
assert to_bin(10) == '1010'
assert to_bin(46685) == '1011011001011101'