import functools

# 29. 순서대로 좌표를 정렬
# functools.cmp_to_key(func)는 sorted()와 같은 정렬 함수의 key 매개변수에 함수(func)를 전달할 때 사용하는 함수다.
# 두 개의 인수를 입력하여 첫 번쨰 인수를 기준으로 그 둘을 비교하여 작으면 음수 같으면 0 크면 양수를 반환한다.
import functools

def xy_compare(n1, n2):
    if n1[1] > n2[1]:         # y 좌표가 크면
        return 1
    elif n1[1] == n2[1]:      # y 좌표가 같으면
        if n1[0] > n2[0]:     # x 좌표가 크면
            return 1
        elif n1[0] == n2[0]:  # x 좌표가 같으면
            return 0
        else:                 # x 좌표가 작으면
            return -1
    else:                     # y 좌표가 작으면
        return -1

src = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
result = sorted(src, key=functools.cmp_to_key(xy_compare))
print(result)

# 30. 웹 페이지를 임시로 저장하려면
# @functools.lru_cache(maxsize=128)은 함수의 반환 결과를 캐시하는 데코레이터이다.
# 최초 요청 이후에는 캐시한 결과를 반환한다.
import urllib.request
from functools import lru_cache

@lru_cache(maxsize=32)
def get_wikidocs(page):
    print("wikidocs page:{}".format(page))  # 페이지 호출시 출력
    resource = 'https://wikidocs.net/{}'.format(page)
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'


first_6 = get_wikidocs(6)
first_7 = get_wikidocs(7)

second_6 = get_wikidocs(6)
second_7 = get_wikidocs(7)

assert first_6 == second_6  # 처음 요청한 6페이지와 두 번째 요청한 6페이지의 내용이 같은지 확인
assert first_7 == second_7

# 31. 기존 함수로 새로운 함수를 만드려면
# functools.parial()은 하나 이상의 인수가 이미 채워진 새 버전의 함수를 만들 때 사용하는 함수다.
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

def add(*args):
    return add_mul('add', *args)

def mul(*args):
    return add_mul('mul', *args)    

print(add(1,2,3,4,5))  # 15 출력
print(mul(1,2,3,4,5))  # 120 출력

from functools import partial
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

add = partial(add_mul, 'add')
mul = partial(add_mul, 'mul')

print(add(1,2,3,4,5))  # 15 출력
print(mul(1,2,3,4,5))  # 120 출력

# 32. 함수를 적용하여 하나의 값으로 줄이려면
# functools.reduce(Function, iterable)은 function을 반복 가능한 객체의 요소에 차례대로 누적 적용하여 이 객체를 하나의 값으로 줄이는 함수다.
def add(data):
    result = 0
    for i in data:
        result += i
    return result

data = [1, 2, 3, 4, 5]
result = add(data)
print(result)

# functools.reduce() 사용
result = functools.reduce(lambda x, y: x + y, data)
print(result)

# functools.reduce()로 최댓값 구하기
num_list = [3,2,8,1,6,7]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
print(max_num)

# 33. 래퍼 함수의 속성을 유지하려면?
# @functools.wraps(wrapped)는 래퍼 함수를 정의할 때 함수의 이름이나 설명문 같은 속성을 유지하도록 하는 데코레이터다.
# 래퍼 함수 : 실제 함수를 감싼 함수로 실제 함수 호출 시 특별한 동작을 하도록 기능을 덧붙인 함수다.

import time
def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행 시간: %f 초" % (end - start))
        return result
    return wrapper

@elapsed
def add(a, b):
    return a + b

result = add(3,4)
print(result)
print(add)

def elapsed(original_func):
    @functools.wraps(original_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        end = time.time()
        print("함수 수행 시간: %f 초" % (end - start))
        return result
    return wrapper

@elapsed
def add(a, b):
    """두 수 a, b를 더한 값을 반환하는 함수"""
    return a + b
print(add)
help(add)

# 34. 다양한 기준으로 정렬
# operator.itemgetter는 sorted와 같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬할 수 있도록 하는 모듈이다.
from operator import itemgetter

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

result = sorted(students, key=itemgetter(1))
print(result)

from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B'),
]

result = sorted(students, key=attrgetter('age'))
print(result)