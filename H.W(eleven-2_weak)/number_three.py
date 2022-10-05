'''
n! 은 1부터 n 까지의 자연수의 곱을 나타내며, 
n 의 계승 또는 팩토리얼<font size="2">factorial</fotn>이라 부른다. 

자연수 n 이 주어졌을 때, n! 의 끝에 있는 0 의 개수를 반환하는 `terminalZeroCount()` 함수를 
작성하라. 
단, n 은 1보다 크고 100보다 작은 자연수라고 가정하며, 문자열 메서드를 활용해야 한다.
'''

# pass 와  None을 적절한 명령문과 표현식으로 대체하라.

def terminalZeroCount(n):
    sum = 1
    zero_sum = 0
    for i in range(1, n+1, 1):
        sum = sum * i
    for letter in str(sum)[::-1]:
        if letter == "0":
            zero_sum = zero_sum + 1
        else:
            break
    return zero_sum

assert terminalZeroCount(5) == 1
assert terminalZeroCount(10) == 2
assert terminalZeroCount(20) == 4