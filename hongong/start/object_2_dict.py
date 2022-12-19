def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

students = [
    create_student("수달", 89, 70, 70, 80),
    create_student("꼬꼬", 100, 70, 100, 90),
    create_student("하파", 79, 30, 50, 60),
    create_student("제비", 80, 50, 60, 73),
    create_student("달님", 60, 100, 90, 85),
    create_student("꽃님", 5, 10, 3, 5)      
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4

    print(student["name"], score_sum, score_average, sep="\t")