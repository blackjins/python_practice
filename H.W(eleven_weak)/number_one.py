'''
양의 정수가 입력되면 1 부터 n 까지의 정수의 합을 구하는 `sum_n()` 함수를 구현하라.
'''
# pass 와 None 을 각각 적절한 명령문과 반환값으로 대체하라.

def sum_n(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i

    return sum



assert sum_n(3) == 6
assert sum_n(5) == 15
assert sum_n(10) == 55
