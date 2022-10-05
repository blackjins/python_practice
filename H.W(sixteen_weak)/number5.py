'''
앞서 사용한 유클리드 호젯법 알고리즘은 양의 정수에 대해서만 옳바르게 작동한다.
예를 들어 아래의 경우처럼 잘못 계산한다. 
참고로 최대공약수는 항상 양수이어야 한다.

```python
>>> gcd(8, -2)
-2
```

이는 음의 분수를 사용할 때 `Fraction` 클래스의 기능에 문제가 발생할 수 있음을 의미한다.

유클리드 호젯법 대신에 다른 알고리즘을 사용하는 `gcd()` 함수를 구현하고
이를 `Fraction` 클래스에 활용하는 예제를 제시하라.
단, 양수, 음수 모두 문제없이 처리해야 한다.
'''
def new_gcd(m, n):
    if n < 0:
        n = -n
    if m < 0:
        m = -m
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        try:
            if isinstance(top, float) or isinstance(bottom, float):
                raise ValueError
            common = new_gcd(top, bottom)
            self.top = top//common
            self.bottom = bottom//common
        except:
            print("정수를 입력 해주세요")


    def __repr__(self):
        return f"{self.top}/{self.bottom}"

    def __add__(self, other_fraction):
        new_top = self.top * other_fraction.bottom + \
                     self.bottom * other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom
        return Fraction(new_top , new_bottom)

    def __eq__(self, other_fraction):
        first_top = self.top * other_fraction.bottom
        second_top = other_fraction.top * self.bottom
        return first_top == second_top
    
    def numerator(self):
        return self.top

    def denominator(self):
        return self.bottom
    
    def to_float(self):
        return self.numerator() / self.denominator()

    def __sub__(self, other_fraction):
        new_top = self.top * other_fraction.bottom - self.bottom * other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom
        
        return Fraction(new_top , new_bottom)
    
    def __mul__(self, other_fraction):
        new_top = self.top * other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom
        return Fraction(new_top, new_bottom)

    def __truediv__(self, other_fraction):
        new_top = self.top * other_fraction.bottom
        new_bottom = self.bottom * other_fraction.top
        return Fraction(new_top, new_bottom)

    def __ne__(self, other_fraction):
        first_top = self.top * other_fraction.bottom
        second_top = other_fraction.top * self.bottom
        return first_top != second_top

    def __gt__(self, other_fraction):
        first_top = self.top * other_fraction.bottom
        second_top = other_fraction.top * self.bottom
        return first_top > second_top

    def __ge__(self, other_fraction):
        first_top = self.top * other_fraction.bottom
        second_top = other_fraction.top * self.bottom
        return first_top >= second_top

    def __lt__(self, other_fraction):
        first_top = self.top * other_fraction.bottom
        second_top = other_fraction.top * self.bottom
        return first_top < second_top

    def __le__(self, other_fraction):
        first_top = self.top * other_fraction.bottom
        second_top = other_fraction.top * self.bottom
        return first_top <= second_top



f1 = Fraction(2, 3)
f2 = Fraction(1, 4)
f3 = Fraction(-2, 4)
f4 = new_gcd(-2, 4)
print(f3, f4)
