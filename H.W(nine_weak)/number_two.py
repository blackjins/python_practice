'''
리스트 또는 튜플에 포함된 수들의 합을 반환하는 함수 `coll_sum()` 를 재귀를 

이용하여 구현하라.
또한 range 자료형도 지원해야 한다. 
'''
sum = 0 
i = 0
def coll_sum(ls):
    global i
    global sum
    if i == 0:
        sum = 0
    num_list = list(ls)
    sum = sum + num_list[i]
    i = i + 1
    if i < len(num_list):
        return coll_sum(num_list)
    i = 0
    return sum
assert coll_sum([1, 2, 3, 4, 5]) == 15
assert coll_sum(range(0, 11, 2)) == 30
assert coll_sum((1.2, 3.3, 5.6, 7.2, 9.8)) == 27.1
