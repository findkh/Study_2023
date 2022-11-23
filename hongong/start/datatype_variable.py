# 변수 만들기 / 사용하기
pi = 3.14159265
print(pi)
print(pi + 2)
print(pi - 2)

# 원의 둘레와 넓이 구하기
r = 10

# 변수 참조
print("원주율 = ", pi)
print("반지름 = ", r)
print("원의 둘레 = ", 2 * pi * r)
print("원의 넓이 = ", pi * r * r)

# 프로그래밍 언어 중 C, C++, 자바, C# 등에서는 변수를 사용할 때 변수의 자료형을 미리 선언해야 한다.
# 파이썬은 변수에 자료형을 지정하지 않고, 같은 변수에 여러 종류의 자료형을 넣을 수 있다.
# 타입 에러가 발생할 수 있으니 가능한 한 변수에는 같은 자료형을 넣어 활용한다.

# 복합 대입 연산자
# => 변수는 내부에 들어 있는 자료의 연산자를 사용할 수 있다.
# 문자열이 들어 있으면 문자열과 관련된 연산자를 사용할 수 있으며, 숫자가 들어 있으면 숫자와 관련된 연산자를 사용할 수 있다.
# 변수를 활용할 때 기존의 연산자와 조합해서 사용할 수 있는 연산자가 복합 대입 연산자다.
number = 100
number += 10
number += 20
number += 30
print("number : ", number)

string = "안녕하세요"
string += "!"
string += "#"
print("string: ", string)

# 사용자 입력: input()
string2 = input("문자 입력")
print(string2)
print(type(string2))

number2 = input("숫자 입력")
print(number2)
print(type(number2)) # 숫자를 입력해도 문자열로 들어온다.

# 문자열을 숫자로 바꾸기(캐스트=cast)
# input() 함수의 입력 자료형은 항상 문자열이기 때문에 입력받은 문자열을 숫자로 변환해야 숫자 연산에 활용할 수 있다.
# int() : 문자열을 int 자료형으로 변환
# float() : 문자열을 float 자료형으로 변환

string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료 : ", string_a + string_b)
print("숫자 자료 : ", int_a + int_b)

# int() 함수와 float() 함수 활용
output_a = int("52")
output_b = float("52.231")

print(type(output_a), output_a)
print(type(output_b), output_b)

# int() 함수와 float() 함수 조합
input_a = float(input("첫번쨰 숫자> "))
input_b = float(input("첫번쨰 숫자> "))

print("덧셈 결과 : ", input_a + input_b)
print("뺄셈 결과 : ", input_a - input_b)
print("곱셈 결과 : ", input_a * input_b)
print("나눗셈 결과 : ", input_a / input_b)

# ValueError 예외
# => 자료형을 변환할 떄 변환할 수 없는 것을 변환하려고 하면 ValueError 예외가 발생한다.
#    숫자가 아닌 것을 숫자로 변환하려고 할 때
#    소수점이 있는 숫자 형식을 문자열을 int() 함수로 변환하려고 할 때

# 숫자를 문자열로 바꾸기 :  str(다른 자료형)
output_c = str(52)
output_d = str(52.123)
print(type(output_c), output_c)
print(type(output_d), output_d)

# inch 단위를 cm으로 바꾸기
# 숫자 입력 받기
raw_input = input("inch 단위의 숫자를 입력해주세요: ")

# 입력 받은 데이터를 숫자 자료형으로 변경 하고 cm로 변경한다.
inch = int(raw_input)
cm = inch * 2.54

print(inch, "inch는 cm 단위로", cm, "cm 입니다.")

# input 변수 스와프
a = input("문자열 입력")
b = input("문자열 입력")
print(a, b)
print(b, a)
print(a[0:], b[0:])
print(b[0:], a[0:])