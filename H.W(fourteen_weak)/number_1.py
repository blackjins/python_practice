'''
`range()` 함수와 동일하게 작동하는 `generate_range()` 제너레이터 함수를 구현하라.
'''
# pass 를 적절한 명령문으로 대체하라.
# 단 일반함수가 아닌 제너레이터로 정의해야 한다.
# 즉, return 이 아닌 yield 키워드가 사용되어야 한다.


def generate_range(end):
    tmp = 0
    if tmp == 0:
            yield tmp
    for i in range(end-1):
        tmp = tmp + 1
        yield tmp
    
assert list(generate_range(5)) == list(range(5))