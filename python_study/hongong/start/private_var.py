# 프라이빗 변수 : 클래스 내부의 변수를 외부에서 사용하는것을 막고 싶을 때 인스턴스 변수 이름을 __변수이름 형태로 선언한다.

import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

circle = Circle(10)
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_area())
print()

print("# __radius에 접근한다.")
print(circle.__radius)
