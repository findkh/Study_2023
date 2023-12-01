# 불 만들기: 비교 연산자
# => 비교 연산자를 통해 만든다.
print(10 == 100)
print(10 != 100)
print(10 <  100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)

# 문자열 비교 연산자.
# 한글은 사전 순서로 앞에 있는것이 작은 값을 갖는다.
print("# 문자열 비교")
print("가방" == "가방")
print("가방" < "하마")
print("가방" > "하마")

# 불 연산 : 논리 연산자
print("# not 연산자")
print(not True)
print(not False)
#연산자 조합
x = 10
under_20 = x < 20
print("under_20: ", under_20)
print("not under_20: ", not under_20)

# if 조건문
number = input("정수 입력> ")
number = int(number)
if number > 0 : print("양수입니다.")
if number < 0 : print("음수입니다.")
if number == 0 : print("0입니다.")

# 날짜/시간 활용하기
import datetime

now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

# 날짜/시간을 한 줄로 출력하기
print("{}년 {}월 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

# 오전과 오후 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.".format(now.hour))
elif now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다".format(now.hour))

# 계절을 구분
if (3 <= now.month <= 5) :
    print("이번 달은 {}월로 봄입니다.".format(now.hour))
elif (6 <= now.month <= 8) :
    print("이번 달은 {}월로 여름입니다.".format(now.month))
elif (9 <= now.month <= 11) :
    print("이번 달은 {}월로 가을입니다.".format(now.month))
else :
    print("이번 달은 {}월로 겨울입니다.".format(now.month))

# 짝수와 홀수 구분하기
number2 = input("정수 입력>")
#last_char = number[-1]
#last_num = int(last_char)
last_num = int(number2)
if (last_num % 2 == 0) :
    print("짝수입니다.")
else :
    print("홀수입니다.")

# 4번 문제
# 숫자 2개 입력 받고 어떤 숫자가 큰지 구하기
a = int(input("> 1번째 숫자: "))
b = int(input("> 2번째 숫자: "))
print()

if(a > b):
    print("첫번째 입력했던 {}가 {}보다 큽니다.".format(a, b))
else:
    print("두번째 입력했던 {}가 {}보다 큽니다.".format(b, a))
