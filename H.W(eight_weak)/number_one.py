'''
자연수 n 이 주어졌을 때, 1의 자릿수가 3의 배수이면 입력값의 세 배를, 아니면 두 배를 반환하는 
함수 `three_or_not()` 함수를 구현하라.

힌트: 나머지 연산자를 활용한다.
'''
# 아래 코드에서 pass 를 적절한 명령문으로, None 을 적절한 표현식으로 대체하라.

def three_or_not(n):
    num = str(n)[::-1]
    num = int(num[0])
    if num%3 == 0:
        return n*3
    else:
        return n*2


assert three_or_not(10) == 30
assert three_or_not(24) == 48