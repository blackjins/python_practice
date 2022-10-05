'''
`Fraction` 클래스의 객체가 항상 기약분수의 형태로 분모와 분자를 사용하도록 
`__init__()` 메서드를 수정하고 활용예제를 제시하라. 

힌트: 최대공약수를 계산하는 함수를 활용해야 한다.
또한 `__add__()` 등 연산 메서드에서 더 이상 기약분수로 변환할 필요가 없어진다.
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
        common = gcd(top, bottom)
        self.top = top//common
        self.bottom = bottom//common

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
f2 = Fraction(1, 4)
assert f1 - f2 == Fraction(5, 12)