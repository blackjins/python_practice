'''
피보나찌 수열은 다음과 같이 정의 된다.

$$
\begin{align*}
F_0 &= 0 \\
F_1 &= 1 \\
F_{n+2} &= F_{n+1} + F_{n}
\end{align*}
$$

for 반복문을 이용하여 피보나찌 수열의 n 번째 값을 반환하는 함수 `fib()` 를 구현하라.
'''
# pass 와 None 을 적절한 명령문과 표현식으로 대체하라.
# 재귀를 사용할 수 없으며 for 반복문만을 이용해야 한다.


def fib(n):
    assert isinstance(n, int)
    assert n >= 0
    fib_list = []
    for i in range(n):
        if i < 2:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        
    return int(fib_list[-1])

assert fib(5) == 5
assert fib(8) == 21
