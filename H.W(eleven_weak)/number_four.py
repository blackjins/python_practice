'''
얌체공을 높은 곳에서 놓아 자연낙하 시키면 바닥에 닿을 때마다 원래 높이의 2/3 만큼 튀어 오른다.
하지만 바닥으로부터 1 cm 이하 높이가 되면 더 이상 튀어오르지 않는다.

얌체공을 n cm 높이에서 자유낙하 시키면 더 이상 튀어오르지 않을 때까지 튀어오른 공의 높이를 모두 
합한 결과를 반환하는 `bouncy()` 함수를 구현하라.
단, 반환값은 소숫점 이하 셋째자리에서 반올림한다.

힌트: [`round()` 함수](https://www.w3schools.com/python/ref_func_round.asp) 참고
'''
# pass 와 None 을 각각 적절한 명령문과 반환값으로 대체하라.

def bouncy(n):
    sum = 0
    if n <= 1:
        return 0
    while True:
        n = n*2/3
        sum = sum + n
        if n < 1:
            break
    return round(sum, 2)

assert bouncy(1) == 0
assert bouncy(2) == 2.22
assert bouncy(10) == 18.24

