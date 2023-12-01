students = [
    {"name": "수달", "korean": 89, "math": 70, "english": 70, "science":80},
    {"name": "꼬꼬", "korean": 100, "math": 70, "english": 100, "science":90},
    {"name": "하파", "korean": 79, "math": 30, "english": 50, "science":60},
    {"name": "제비", "korean": 80, "math": 50, "english": 60, "science":73},
    {"name": "달님", "korean": 60, "math": 100, "english": 90, "science":85},
    {"name": "꽃님", "korean": 5, "math": 10, "english": 3, "science":5},
]

print("이름", "총점", "평균", sep="\t")

for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_avg = score_sum / 4
    print(student["name"], score_sum, score_avg, sep="\t")