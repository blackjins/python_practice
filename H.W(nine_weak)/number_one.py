'''
양의 정수들의 최대공약수(gcd)를 반환하는 함수 `gcd()` 를 재귀를 이용하여 구현하라.

힌트: 유클리드 호제법을 활용한다.
'''
tmp = -1
def gcd(x, y):
    assert isinstance(x, int) & (x > 0)
    assert isinstance(y, int) & (y > 0)
    if x%y == 0:
        if x > y:
            return y
        if x < y:
            return x
    elif x%y != 0:
        if x > y:
            tmp = y
            x = x%y
            return gcd(tmp, x)
        if x < y:
            tmp = x
            y = y%x
            return gcd(tmp, y)
    
assert gcd(14, 18) == 2
assert gcd(90, 72) == 18
assert gcd(24, 30) == 6
