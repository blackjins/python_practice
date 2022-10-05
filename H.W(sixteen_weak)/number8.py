'''
컴퓨터가 제공하는 부동소수점은 불완전하다.
예를 들어, 아래 코드는 10분의 1을 10번 더했을 때 
1이 계산되지 않음을 보여준다.
x = 0.1
y = 0

for _ in range(10): 
    y += x
    
print(y)    
print(y == 1.0)
분수 클래스 `Fraction`를 이용하면 보다 엄밀한 계산이 가능함을 보여라.

힌트: `to_float()` 메서드 활용
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

    def to_float(self):
        return self.numerator() / self.denominator()



fx = Fraction(1, 10)
fy = Fraction(0, 1)
fx.to_float()

for _ in range(10):
    fy += fx

assert fy.to_float() == 1.0