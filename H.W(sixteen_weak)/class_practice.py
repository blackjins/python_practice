from configparser import SectionProxy


class Calculus:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.result = 0

    def add(self):
        self.result = self.first + self.second
        return self.result

    def mul(self):
        self.result = self.first * self.second
        return self.result

    def min(self):
        self.result = self.first - self.second
        return self.result

test = Calculus(3, 5)
print(test.add())
print(test.mul())
print(test.min())