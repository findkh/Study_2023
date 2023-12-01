# getter와 setter는 프라이빗 변수의 값을 추출하거나 변경할 목적으로 간접적으로 속성에 접근하도록 해주는 함수다.
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # 게터 세터 선언
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value

circle = Circle(10)
print("# 원의 둘레와 넓이를 구한다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

print("# 간접적으로 __radius 접근")
print(circle.get_radius())
print()

circle.set_radius(2)
print("#반지름을 변경하고 원의 둘레와 넓이를 구한다.")
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_area())