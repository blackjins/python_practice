'''
페르마의 마지막 정리는 정수 n 이 2보다 클 때, 
아래 식을 만족하는 세 개의 양의 정수 a, b, c 가 존재하지 않는다고 말한다.

a^n + b^n = c^n 

n, a, b, c 네 개의 값이 주어졌을 때 위 등식이 성립하는지 여부를 판단하는 함수
`fermat()` 를 구현하라.
단, 다음 조건을 만족해야 한다.

- `n`, `a`, `b`, `c` 네 개의 매개변수를 사용한다.
- `n` 에 2보다 같거나 작은 수가 인자로 사용되면 `False`를 반환한다.
- `n` 에 2보다 큰 경우 위 식이 성립하면 `True`, 아니면 `False` 를 반환한다.
'''
# 아래 코드에서 pass 를 적절한 명령문으로, None 을 적절한 표현식으로 대체하라.

def fermat(n, a, b, c):
    if n <= 2:
        return False
    if n > 2:
        if a**n + b**n == c**n:
            return True
        else:
            return False
        
    return None

assert fermat(2, 3, 5, 7) == False
assert fermat(3, 17, 3, 22) == False

