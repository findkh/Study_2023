class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("=========학생 목록=========")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------- ------- -------")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

Student("수달", 89, 70, 70, 80),
Student("꼬꼬", 100, 70, 100, 90),
Student("하파", 79, 30, 50, 60),
Student("제비", 80, 50, 60, 73),
Student("달님", 60, 100, 90, 85),
Student("꽃님", 5, 10, 3, 5),
Student("수달2", 89, 70, 70, 80),
Student("꼬꼬2", 100, 70, 100, 90),
Student("하파2", 79, 30, 50, 60),
Student("제비2", 80, 50, 60, 73),
Student("달님2", 60, 100, 90, 85),
Student("꽃님2", 5, 10, 3, 5)

Student.print()