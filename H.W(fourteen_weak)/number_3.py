'''
이번엔 인자를 세 개 사용해도 
`range()` 함수와 동일하게 작동하는 `generate_range()` 제너레이터 함수를 구현하라.
'''
# pass 를 적절한 명령문으로 대체하라.
# 단 일반함수가 아닌 제너레이터로 정의해야 한다.
# 즉, return 이 아닌 yield 키워드가 사용되어야 한다.

def generate_range(start, end, step):
    tmp = start
    yield tmp
    for i in range(end//step-1):
        tmp = tmp + step
        yield tmp
assert list(generate_range(1, 5, 2)) == list(range(1, 5, 2))