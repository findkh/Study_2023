class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

Students = [
    Student("수달", 89, 70, 70, 80),
    Student("꼬꼬", 100, 70, 100, 90),
    Student("하파", 79, 30, 50, 60),
    Student("제비", 80, 50, 60, 73),
    Student("달님", 60, 100, 90, 85),
    Student("꽃님", 5, 10, 3, 5)      
]

print()
print("현재 생성된 총 학생수는 {}명입니다.".format(Student.count))