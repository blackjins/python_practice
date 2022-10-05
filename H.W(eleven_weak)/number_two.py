'''
양의 정수가 입력되면 1 부터 n 까지의 정수의 제곱의 합을 구하는 `square_sum()` 함수를 구현하라.
'''

# pass 와 None 을 각각 적절한 명령문과 반환값으로 대체하라.

def square_sum(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i**2      

    return sum


assert square_sum(1) == 1
assert square_sum(3) == 14
assert square_sum(5) == 55
