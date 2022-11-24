# 문자열의 format() 함수
# 중괄호를 포함한 문자열 뒤에 마침표를 찍고 format() 함수 사용
# 중괄호 개수와 format 함수 괄호 안 매개변수의 개수는 반드시 같아야 한다.

# format() 함수로 숫자가 문자열로 변환하기
string_a = "{}".format(10)
print(string_a)
print(type(string_a))

# format() 함수의 다양한 형태
format_a = "{}만원".format(5000)
format_b = "파이썬으로 열공하여 연봉 {}만 원 올리기".format(2000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

# IndexError 예외
# => {} 기호의 개수가 format()함수의 매개변수 개수보다 많으면 IndexError 예외가 발생한다.

# 정수를 특정 칸에 출력하기
output_a = "{:d}".format(52)

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)

# 기호 붙여 출력하기
output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)

print("# 기호 붙여 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)

# 조합하기
output_h = "{:+5d}".format(52)
output_i = "{:+5d}".format(-52)
output_j = "{:=+5d}".format(52)
output_k = "{:=+5d}".format(-52)
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52)

print("# 조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)

# 부동 소수점 출력하기
outputF_a = "{:f}".format(52.273)
outputF_b= "{:15f}".format(-52.273)
outputF_c = "{:+15f}".format(52.273)
outputF_d = "{:+015f}".format(52.273)

print(outputF_a)
print(outputF_b)
print(outputF_c)
print(outputF_d)

# 소수점 아래 자릿수 지정하기 - 자동 반올림됨
outputF_e = "{:15.3f}".format(52.273)
outputF_f = "{:15.2f}".format(52.273)
outputF_g = "{:15.1f}".format(52.273)

print(outputF_e)
print(outputF_f)
print(outputF_g)

# 의미 없는 소수점 제거하기
outputF_h = 52.0
outputF_i = "{:g}".format(outputF_h)
print(outputF_h)
print(outputF_i)

# 대소문자 바꾸기 : upper(), lower()
a = "Hello Python Programing"
print(a.upper())
print(a.lower())

# 문자열 공백 제거
# strip() : 문자열 양옆의 공백 제거
# lstrip() : 문자열 왼쪽의 공백 제거
# rstrip() : 문자열 오른쪽의 공백 제거
input_a = """
    안녕하세요
파이썬 공부하는 수달입니다.
"""
print(input_a)
print(input_a.strip())

# 문자열 구성 파악하기
# isalnum() : 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인
# isalpha() : 문자열이 알파벳으로만 구성되어 있는지 확인
# isidentifier() : 문자열이 식별자로 사용할 수 있는지 확인
# isdecimal() : 문자열이 정수 형태인지 확인
# isdigit() : 문자열이 숫자로 인식될 수 있는지 확인
# isspace() : 문자열이 공백으로만 구성되어 있는지 확인
# islower() : 문자열이 소문자로만 구성되어 있는지 확인
# isupper() : 문자열이 대문자로만 구성되어 있는지 확인

print("TrainA10".isalnum())
print("TrainA10".isalpha())
print("10".isdigit())

# 문자열 찾기
# find() : 왼쪽부터 찾아서 처음 등장하는 위치를 찾는다.
# rfind() : 오른쪽부터 찾아서 처음 등장하는 위치를 찾는다.
print("안녕안녕하세요".find("안녕")) # 0
print("안녕안녕하세요".rfind("안녕")) # 2

# 문자열과 in 연산자
# 문자열 내부에 문자열 확인할 때 사용. True/False 반환
print("안녕" in "안녕하세요")
print("잘자" in "수달입니다")

# 문자열 자르기 : split()
# 실행 결과는 리스트로 나온다.
b = "10 20 30 40 50".split(" ")
print(b)

# f-문자열
# f'문자열{표현식}문자열'
print(f"3 + 4 = {3+4}")

# f-문자열보다 format()함수를 사용하는 경우
# - 문자열 내용이 너무 많을 때
# - 데이터를 리스트에 담아서 사용할 때

# 마무리
# 3번 문제
a = input("> 1번쨰 숫자: ")
b = input("> 2번째 숫자: ")

print()
print("{} + {} = {}".format(a, b, int(a)+int(b)))

# 4번 문제
string = "hello"
string.upper()
print("A 지점:", string)
print("B 지점", string.upper())

# 구의 부피와 겉넓이를 구하는 프로그램
pi = 3.141592
r = input("구의 반지름을 입력해주세요: >")
v = 4/3*pi*int(r)*int(r)*int(r)
s = 4*pi*int(r)*int(r)
print("구의 부피는 {:.13f} 입니다.".format(v))
print("구의 겉넓이는 {:.4f} 입니다.".format(s))

# 피타고라스의 정리
b = input("밑변의 길이를 입력해주세요: >") 
h = input("높이의 길이를 입력해주세요: >")
print((float(b) * float(b)))
print((float(h) * float(h)))
print("빗변의 길이는 {:.1f} 입니다.".format(((float(b) * float(b)) + (float(h) * float(h))) ** (1/2)))