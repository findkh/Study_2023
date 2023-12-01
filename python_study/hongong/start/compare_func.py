class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le_____(self, value):
        return self.get_sum() <= value.get_sum()

students = [
    Student("수달", 89, 70, 70, 80),
    Student("꼬꼬", 100, 70, 100, 90),
    Student("하파", 79, 30, 50, 60),
    Student("제비", 80, 50, 60, 73),
    Student("달님", 60, 100, 90, 85),
    Student("꽃님", 5, 10, 3, 5)      
]

student_a = Student("수달", 89, 70, 70, 80),
student_b = Student("꼬꼬", 100, 70, 100, 90),

print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a  > student_b = ", student_a > student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a  < student_b = ", student_a < student_b)
print("student_a <= student_b = ", student_a <= student_b)