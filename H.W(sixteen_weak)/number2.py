'''
`Fraction` 클래스가 크기비교를 지원하도록
다음 비교 연산자들을 구현하라.

* `__ne__()`
* `__gt__()`
* `__ge__()`
* `__lt__()`
* `__le__()`
'''
def gcd(m, n):
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
        self.top = top
        self.bottom = bottom

    def __repr__(self):
        return f"{self.top}/{self.bottom}"

    def __add__(self, other_fraction):
        new_top = self.top * other_fraction.bottom + \
                     self.bottom * other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom
        common = gcd(new_top, new_bottom)
        
        return Fraction(new_top // common, new_bottom // common)

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
        common = gcd(new_top, new_bottom)
        
        return Fraction(new_top // common, new_bottom // common)

    def __mul__(self, other_fraction):
        new_top = self.top * other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom
        common = gcd(new_top, new_bottom)
        return Fraction(new_top//common, new_bottom // common)

    def __truediv__(self, other_fraction):
        new_top = self.top * other_fraction.bottom
        new_bottom = self.bottom * other_fraction.top
        common = gcd(new_top, new_bottom)
        return Fraction(new_top//common, new_bottom // common)

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
f3 = Fraction(1, 4)
# 아래 코드의 주석을 해제하고 실행하라.
assert (f1 != f3) == True
assert (f1 > f3) == True
assert (f1 >= f3) == True
assert (f1 < f3) == False
assert (f1 <= f3) == False