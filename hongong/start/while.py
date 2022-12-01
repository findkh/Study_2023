# # 범위 자료형과 while 반복문
# # 범위 자료형
# # => 정수로 이루어진 범위를 만들 때는 range() 함수를 사용한다.
# # 1. 매개변수에 숫자를 한개 넣는 방법
# #   range(A)
# # 2. 매개변수에 숫자를 두개 넣는 방법 : A부터 B-1까지의 정수로 범위를 만든다
# #   range(A, B)
# # 3. 매개변수에 숫자를 세 개 넣는 방법 : A부터 B-1까지의 정수인데 앞 뒤의 숫자가 C만큼 차이를 가진다.
# #   range(A, B, C)

# a = range(5)
# print(a)
# print(list(a))

# print(list(range(0,5)))
# print(list(range(0,10,2)))

# # range() 함수의 매개변수는 반드시 정수를 사용해야 한다. TypeError 발생
# n = 10
# a = range(0, int(n/2))
# print(list(a))

# b = range(0, n//2) # // -> 정수 나누기 연산자
# print(list(b))

# # for 반복문 : 범위와 함께 사용하기
# # for 숫자 변수 in 범위 :
# #   코드

# for i in range(5):
#     print(str(i) + "=반복 변수")
# print()

# for i in range(5, 10):
#     print(str(i) + "=반복 변수")
# print()

# for i in range(0, 10, 3):
#     print(str(i) + "=반복 변수")
# print()

# array = [273, 32, 103, 14, 27]

# for i in range(len(array)):
#     print("{}번째 반복 : {}".format(i, array[i]))

# # 반대로 반복
# for i in range(4, 0 - 1, -1):
#     print("현재 반복 변수: {}".format(i))


# for i in range(len(array)-1, -1, -1):
#     print("{}번쨰 반복: {}".format(i, array[i]))

# # reversed() 사용
# for i in reversed(range(5)):
#     print(i)

# # 피라미드만들기
# for i in range(10):
#     print(i * "*")

# # 중첩 반복문 사용
# for i in range(10):
#     star = ""
#     for j in range(i):
#        star += "*"
#     print(star)

# print()
# # 공백 포함 피라미드 만들기
# for i in range(1, 5):
#     star = ""
#     for j in range(4, i, -1):
#         star += " "
#     for k in range(0, 2 * i -1):
#         star += "*"
#     print(star)

# # while 반복문
# # => 불표현식이 참인동안 문자을 반복
# # while 불 표현식:
# #   문장
# i = 0
# while i < 10:
#     print("{}번째 반복입니다.".format(i))
#     i += 1

# # 상태를 기반으로 반복하기
# list_test = [1,2,1,2]
# value = 2
# while value in list_test:
#     list_test.remove(value)

# print(list_test)

# # 시간을 기반으로 반복하기
# # 유닉스 타임 : 세계 표준시(UTC)로 1970년 1월 1일 0시 0분 0초를 기준으로 몇 초가 지났는지 정수로 나타낸다.
# import time
# print(time.time())

# # 5초 동안 반복하기
# number = 0

# target_tick = time.time()+5
# while time.time() < target_tick:
#     number += 1

# print("5초 동안 {}번 반복했습니다.".format(number))

# # break, continue 키워드
# i = 0

# while True:
#     print("{}번째 반복문입니다.".format(i))
#     i = i + 1
#     input_text = input("> 종료하시겠습니까?(y/n)")
#     if input_text in ["y", "Y"]:
#         print("반복을 종료합니다.")
#         break

# # continue 키워드
# numbers = [5, 15, 6, 20, 7, 25]

# for number in numbers:
#     if number < 10:
#         continue
#     print(number)

# # 확인 문제1
# print(list(range(4, 6)))
# print(list(range(7, 0, -1)))
# #[3,6,9]
# print(list(range(3,10,3)))

# 확인 문제2
# 리스를 조합하여 딕셔너리 만들기
# key_list = ["name", "hp", "mp", "level"]
# value_list = ["기사", 200, 30, 5]
# character = {}

# for i in range(len(key_list)):
#     character[key_list[i]] = value_list[i]
# print(character)

# # 확인 문제3
# # 1부터 숫자를 하나씩 증가시키면서 몇을 더할 때 1000을 넘기는지 출력
# limit = 10000
# i = 1
# sum_value = 0
# while True :
#     sum_value += i
#     i = i + 1
#     if sum_value > limit:
#         print("{}을 더할 때 {}이 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))
#         break

# 확인문제4
# 1부터 100까지의 숫자가 있다.
# 1 * 99, 2 * 98, 3 * 87 ... 98 * 2, 99 * 1
# 위와 같이 계산 될 때 최대가 되는 경우는 어떤 숫자를 곱했을 때인지 찾기

max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i
    
    if max_value < i*j:
        max_value = i * j
        a = i
        b = j
    else:
        continue
        

print("최대가 되는 경우 : {} * {} = {}".format(a, b, max_value))
