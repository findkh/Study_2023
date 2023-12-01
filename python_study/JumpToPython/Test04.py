# # 1. 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수 작성
# def is_odd(number):
#     if number % 2 != 0:
#         return True
#     else:
#         return False

# print(is_odd(3))
# print(is_odd(2))

# # 2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성(입력값의 개수는 정해져 있지 않다.)
# def avg_numbers(* args):
#     result = 0
#     for i in args:
#         result += i
#     return result / len(args)

# print(avg_numbers(1, 2))
# print(avg_numbers(1,2,3,4,5))

# # 3. 두 개의 숫자를 입력 받아 더하여 돌려주는 프로그램이다. 오류를 수정해라
# input1 = int(input("첫번째 숫자를 입력"))
# input2 = int(input("두번째 숫자를 입력"))

# total = input1 + input2
# print("두 수의 합은 %s 입니다." % total)

# # 4. 다음 중 출력 결과가 다른 것 -> 3번
# print('you' 'need' 'python')
# print('you' + 'need' + 'python')
# print('you', 'need', 'python')
# print("".join(['you', 'need', 'python']))

# # 5. test2.txt 파일에 Life is too short 문자열을 저장한 후 그 파일을 읽어서 출력하는 프로그램이다. 오류를 수정해라
# f1 = open("test2.txt", "w")
# f1.write("Life is too short")
# f1.close()

# f2 = open("test2.txt", "r")
# data = f2.read()
# print(data)
# f2.close()

# # 6. 사용자의 입력을 파일에 저장하는 프로그램을 작성
# # 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.
# user_input = input("저장할 내용을 입력하세요> ")
# f = open("test2.txt", "a", encoding="utf-8")
# f.write("\n"+ user_input)
# f.write("\n")
# f.close()

# 7. 파일의 내용 중 java 라는 문자열을 python으로 바꾸어 저장
f3 = open("test2.txt", "r", encoding="UTF-8")
body = f3.read()
f3.close

body = body.replace("java", "python")

f4 = open("test2.txt", "w", encoding="UTF-8")
f4.write(body)
f4.close()

