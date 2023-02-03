# 44. 객체를 파일로 저장하고 불러오려면?
# pickle은 파이썬에서 사용하는 딕셔너리, 리스트, 클래스 등의 자료형을 변환 없이 그대로 파일로 저장하고 이를 불러올 때 사용하는 모듈이다.
import pickle

# def get_all_data():
#     try:
#         with open("data.p", 'rb') as f: 
#             return pickle.load(f)
#     except FileNotFoundError:
#         return {}


# def add_data(no, subject, content):
#     data = get_all_data()
#     assert no not in data
#     data[no] = {'no': no, 'subject': subject, 'content': content}
#     with open('data.p', 'wb') as f:
#         pickle.dump(data, f)


# def get_data(no):
#     data = get_all_data()
#     return data[no]


# # 데이터저장
# add_data(1, '안녕 피클', '피클은 매우 간단합니다.')

# # 데이터조회
# data = get_data(1)
# print(data['no'])
# print(data['subject'])
# print(data['content'])

# 45. 객체 변경에 따른 오류를 방지하려면?
# copyreg는 pickle로 저장한 객체를 불러올 때 객체를 생성하는 함수다.
import copyreg

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# def pickle_student(student):
#     kwargs = student.__dict__
#     return unpickle_student, (kwargs, )

# def unpickle_student(kwargs):
#     return Student(**kwargs)

# copyreg.pickle(Student, pickle_student)

# a = Student('임철희', 27)
# with open('student.p', 'wb') as f:
#     pickle.dump(a, f)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.dummy = 'dummy'  # dummy 속성을 새로 추가!


# def pickle_student(student):
#     kwargs = student.__dict__
#     return unpickle_student, (kwargs, )


# def unpickle_student(kwargs):
#     return Student(**kwargs)


# copyreg.pickle(Student, pickle_student)

# with open('student.p', 'rb') as f:
#     student = pickle.load(f)  # unpickle_student() 함수를 호출한다.

# print(student.dummy)

# 46. 딕셔너리를 파일로 저장하려면?
# shelve는 딕셔너리를 파일로 저장할 때 사용하는 모듈로 키에 해당하는 값을 저장할 수 있다. 파이썬의 모든 객체를 값으로 저장할 수 있다.
import shelve


def save(key, value):
    with shelve.open('shelve.dat') as d:
        d[key] = value

def get(key):
    with shelve.open('shelve.dat') as d:
        return d[key]

save('number', [1, 2, 3, 4, 5])
print(get('number')) 