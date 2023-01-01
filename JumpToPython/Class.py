class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

class FourCal:
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
a.setData(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

# 생성자
# => 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.
class FourCal2:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal2(4, 2)
print(a.first)
print(a.second)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

# 상속
class MoreFourCal(FourCal2):
    def pow(self): 
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal2):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

# a = FourCal2(4, 0)
# print(a.div())
a = SafeFourCal(4, 0)
print(a)
