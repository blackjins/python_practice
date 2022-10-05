'''
임의로 중첩된 리스트를 풀어헤쳐 중첩이 없는 리스트를 생성하는
`flatten()` 함수를 제너레이터 함수를 이용하여 구현하라.
단, 재귀를 이용할 수 있다.

참고: [stackoverflow: 임의로 중첩된 리스트 납작하게 만들기](https://stackoverflow.com/questions/10823877/what-is-the-fastest-way-to-flatten-arbitrarily-nested-lists-in-python)
'''
# pass 를 적절한 명령문으로 대체하라.
# 단 일반함수가 아닌 제너레이터로 정의해야 한다.
# 즉, return 이 아닌 yield 키워드가 사용되어야 한다.
nests = [1, 2, [3, 4, [5],['hi']], [6, [[[7, 'hello']]]]]
def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i
assert list(flatten(nests)) == [1, 2, 3, 4, 5, 'hi', 6, 7, 'hello']
