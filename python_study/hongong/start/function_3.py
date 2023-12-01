# 함수 고급
# 튜플 : 리스트와 비슷한 자료형, 한번 결정된 요소는 바꿀 수 없다.
tuple_test = (10, 20, 30)
print(tuple_test[0])
print(tuple_test[2])

# 요소를 하나만 가지는 튜플
print(type((273))) # <class 'int'>
print(type((273,))) # <class 'tuple'>

# 리스트와 튜플의 특이한 사용
# 리스트와 튜플 변수 할당
[a,b] = [10, 20]
(c,d) = (10, 20)
print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)

# 튜플은 괄호를 생략해도 튜플로 인식할 수 있는 경우 생략해도 된다.
# 괄호가 없는 튜플
tuple_test2 = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test2 : ", tuple_test2)
print("type(type_test2) : ", type(tuple_test2))
print()

# 괄호가 없는 튜플 활용
a, b, c = 10, 20, 30
print("# 괄호가 없는 튜플 활용")
print("a: ", a)
print("b: ", b)
print("c: ", c)

# 변수의 값을 교환하는 튜플
a, b = 10, 20
print("# 교환 전")
print("a: ", a)
print("b: ", b)

# 값 교환
a, b = b, a
print("# 교환 후 값")
print("a: ", a)
print("b: ", b)

# 튜플과 함수
# => 튜플은 함수의 리턴에 많이 사용한다.
def test():
    return (10, 20)

a, b = test()
print("a: ", a)
print("b: ", b)

# 튜플 리턴 예
for i, value in enumerate([1,2,3,4,5,6,7,8]):
    print("{}번째 요소는 {}입니다.".format(i, value))

a, b = 97, 30
print(a // b)

a, b = 97, 40
x, y = divmod(a, b)
print(x)
print(y)

# 람다
# 함수의 매개변수에 사용하는 함수를 콜백 함수라고 한다.
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕")

call_10_times(print_hello)

# filter()함수와 map() 함수
# map() : 리스틔 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해주는 함수다.
#   map(함수, 리스트)
# filter() : 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로, 새로운 리스트를 구성해주는 함수다.
#   filter(함수, 리스트)

def power(item):
    return item * item
def under_3(item):
    return item < 3

list_input_a = [1,2,3,4,5]

# map() 함수 사용
output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a): ", output_a)
print("map(power, list_input_a): ", list(output_a))
print()

# filter() 함수 사용
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행결과")
print("map(under_3, list_input_a): ", output_a)
print("map(under_3, list_input_a): ", list(output_b))
print()

# 람다의 개념
# lambda 매개변수: 리턴값
# def 키워드로 선언했던 함수를 lambda로 바꾸고, return 키워드를 쓰지 않는다.
power = lambda x : x * x
under_3 = lambda x : x < 3

list_input_a = [1,2,3,4,5]
# map() 함수 사용
output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a): ", output_a)
print("map(power, list_input_a): ", list(output_a))
print()

# filter() 함수 사용
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행결과")
print("map(under_3, list_input_a): ", output_a)
print("map(under_3, list_input_a): ", list(output_b))
print()

# 인라인 람다
# map() 함수 사용
output_a = map(lambda x : x * x, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a): ", output_a)
print("map(power, list_input_a): ", list(output_a))
print()

# filter() 함수 사용
output_b = filter(lambda x : x < 3, list_input_a)
print("# filter() 함수의 실행결과")
print("map(under_3, list_input_a): ", output_a)
print("map(under_3, list_input_a): ", list(output_b))
print()

# 파일 처리
# 파일 열고 닫기
#   파일 객체 = open(문자열: 파일경로, 문자열: 읽기 모드)
#        w : write 모드(새로 쓰기 모드)
#        a : append 모드(뒤에 이어서 쓰기 모드)
#        r : read 모드(읽기 모드)
# 파일 닫기
#   파일객체.close()

file = open("basic.txt", "w")
file.write("Hello Python Programming!")
file.close()

# with 키워드
#   => open()함수와 close() 함수 사이에 코드가 많이 들어가면 파일을 열고 닫는 실수를 하는 경우가 생긴다.
#       이를 방지 하기 위해 사용한다.
#   with open(문자열: 파일경로, 문자열: 모드) as 파일 객체:
#       문장

with open("basic.txt", "w") as file:
    file.write("Hello..2")

# 텍스트 읽기
#   파일 객체.read()
with open("basic.txt", "r") as file:
    contents = file.read()
print(contents)

# 텍스트 한 줄씩 읽기
# 랜덤으로 1000명의 키와 몸무게 만들기
import random
hanguls = list("가나다라마바사아자차카타파하")
with open("info.txt", "w", encoding="UTF-8") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))

# 반복문으로 파일 한줄씩 읽기
with open("info.txt","r", encoding="UTF-8") as file:
    for line in file:
        (name, weight, height) = line.strip().split(",")

        if(not name) or (not weight) or (not height):
            continue
        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()