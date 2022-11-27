# else 조건문의 활용
# if 조건:
#   조건이 참일때 실행할 문장
# else:
#   조건이 거짓일떄 실행할 문장

# if 조건문 활용
score = float(input("점수 입력> "))
if (score == 4.5):
    print("신")
elif(score >= 4.2):
    print("교수님의 사랑")
elif(score >= 3.5):
    print("현 체제의 수호자")
elif(score >= 2.8):
    print("일반인")
elif(score >= 2.3):
    print("일탈을 꿈꾸는 소시민")
elif(score >= 1.75):
    print("오락문화 선구자")
elif(score >= 1.0):
    print("불가촉천민")
elif(score >= 1.0):
    print("자벌레")
elif(score >= 0.5):
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗")

# False로 변환되는 값
# => Flase로 변환되는 값은 None, 숫자 0과 0.0, 빈 컨테이너(빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리 등)
print("# if 조건문에 0 넣기")
if 0:
    print("0은 True로 변환됩니다.")
else :
    print("0은 False로 변환됩니다.")
    print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다.")
else :
    print("빈 문자열은 False로 변환됩니다.")

# pass 키워드
# 나중에 구현하려고 비워 둔 구문
number = int(input("정수 입력> "))

if number > 0:
    # 양수 일때 : 미구현
#else : #IndentationError: expected an indented block after 'if' statement on line 49
    # 음수일 때 : 미구현
    pass
else :
    pass

# raise NotImplementedError
# => pass 키워드 입력 해놓은 곳에 구현하지 않은 부분이라고 오류를 강제로 발생 시킬 때 사용

# 확인 문제1
x = 2
y = 10
if x > 4:
    if y > 2:
        print(x * y)
else:
    print(x+y)

x = 1
y = 4
if x > 4:
    if y > 2:
        print(x * y)
else:
    print(x + y)

x = 10
y = 2
if x > 4:
    if y > 2:
        print(x * y)
else:
    print(x + y)

# 확인 문제2
x = 15
if(x > 10 and x < 20):
    print("조건에 맞습니다.")

# 확인 문제3
# 태어난 연도를 입력 받아 띠를 출력
str_input = int(input("태어난 해를 입력해주세요>"))
birth_year = str_input % 12

if birth_year == 0:
    print("원숭이 띠")
elif birth_year == 1:
    print("닭 띠")
elif birth_year == 2:
    print("개 띠")
elif birth_year == 3:
    print("돼지 띠")
elif birth_year == 4:
    print("쥐 띠")
elif birth_year == 5:
    print("소 띠")
elif birth_year == 6:
    print("범 띠")
elif birth_year == 7:
    print("토끼 띠")
elif birth_year == 8:
    print("용 띠")
elif birth_year == 9:
    print("뱀 띠")
elif birth_year == 10:
    print("말 띠")
else:
    print("양 띠")

# 도전 문제 1
# 간단한 대화 프로그램
import datetime

q = input("입력> ")
if "안녕" in q:
    print("안녕하세요.")
elif "몇 시" in q:
    print("지금은 {}시입니다.".format(datetime.datetime.now().hour))
else:
    print(q)

# 도전 문제 2
# 2, 3, 4, 5로 나누어 떨어지는지 확인하고 출력
str = int(input("정수를 입력해주세요> "))

if(str % 2 == 0):
    print("2로 나누어 떨어지는 숫자입니다.")
else:
    print("2로 나누어 떨어지는 숫자가 아닙니다.")

if(str % 3 == 0):
    print("3로 나누어 떨어지는 숫자입니다.")
else:
    print("3로 나누어 떨어지는 숫자가 아닙니다.")

if(str % 4 == 0):
    print("4로 나누어 떨어지는 숫자입니다.")
else:
    print("4로 나누어 떨어지는 숫자가 아닙니다.")

if(str % 5 == 0):
    print("5로 나누어 떨어지는 숫자입니다.")
else:
    print("5로 나누어 떨어지는 숫자가 아닙니다.")