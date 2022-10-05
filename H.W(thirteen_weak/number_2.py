'''
리스트가 입력되면 중복된 항목은 제거하고 남은 항목들을 내림차순으로 정렬한
리스트를 반환하는 `unique_values()` 함수를 구현하라. 
'''

# pass 와  None을 적절한 명령문과 표현식으로 대체하라.

def unique_values(aList):
    aList = list(set(aList))
    aList.sort(reverse=True)    


    return aList

assert unique_values([1, 2, 1, 3]) == [3, 2, 1]
assert unique_values(['z', 'f', 'a', 'z']) == ['z', 'f', 'a']
