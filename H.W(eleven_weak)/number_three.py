'''
양의 정수가 입력되면 1 부터 n 까지의 정수의 제곱의 합을 
음의 정수가 입력되면 n 부터 -n 까지의 정수의 제곱의 합을 구하는 `square_sum_abs()` 함수를 구현하라.
'''

# pass 와 None 을 각각 적절한 명령문과 반환값으로 대체하라.

def square_sum_abs(n):
    if n > 0 :
        sum = 0
        for i in range(n+1):
            sum = sum + i**2
    elif n < 0:
        sum = 0
        for i in range(n, -n +1):
            sum = sum + i**2
    elif n == 0:
        raise Exception
    return sum


assert square_sum_abs(-1) == 2
assert square_sum_abs(-3) == 28
assert square_sum_abs(5) == 55
assert square_sum_abs(-5) == 110