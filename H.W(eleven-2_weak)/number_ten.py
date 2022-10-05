'''
리스트을 항목을 내림차순으로 정렬한 값을 반환하는 `rev_list()` 함수를 구현하라.
'''
# pass 와  None을 적절한 명령문과 표현식으로 대체하라.

def rev_list(aList):
    aList.sort(reverse=True)

    return aList


assert rev_list([2, 4, 1, 2]) == [4, 2, 2, 1]
assert rev_list(['c', 'f', 'a']) == ['f', 'c', 'a']
assert rev_list(['_ff', 'ABC', 'abd']) == ['abd', '_ff', 'ABC']