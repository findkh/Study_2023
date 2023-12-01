# 오류의 종류
# 프로그램 실행 전, 실행 중 발생하는 오류가 있다.
# 실행 전 발생하는 오류를 구문오류
# 실행 중 발생하는 오류를 예외 또는 런타임 오류라고 한다.

# 구문 오류
# SyntaxError는 구문에 문제가 있어 프로그램이 실행조차 되지 않는 오류다.
# 구문 오류는 해결하지 않으면 프로그램 자체가 실행되지 않는다.

# 기본 예외 처리
# 예외를 해결하는 모든 것을 예외 처리라고 부른다.
# 조건문을 사용, try 구문을 사용

# # 조건문으로 예외 처리하기
user_input_a = input("정수 입력> ")

if user_input_a.isdigit():
    number_input_a = int(user_input_a)

    print("원의 반지름:", number_input_a)
    print("원의 둘레: ", 2 * 3.14 * number_input_a)
    print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
else :
    print("정수를 입력하지 않았습니다.")

# try exception 구문
try:
    number_input_a = int(input("정수 입력: >"))
    print("원의 반지름:", number_input_a)
    print("원의 둘레: ", 2 * 3.14 * number_input_a)
    print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
except:
    print("무언가 잘못되었습니다.")

# try exception 구문과 pass 키워드 조합
# 숫자로 변환되는 것들만 리스트에 넣기
list_input_b = ["52", "수달", "32", "스파이", "103"]
list_num = []
for item in list_input_b:
    try:
        float(item)
        list_num.append(item)
    except:
        pass

print("{}내부에 있는 숫자는".format(list_input_b))
print("{}입니다.".format(list_num))

# try except else 구문
# try:
#   예외가 발생할 가능성이 있는 코드
# except:
#   예외가 발생했을 때 실행할 코드
# else :
#   예외가 발생하지 않았을 때 실행할 코드

try:
    number_input_c = int(input("정수 입력> "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름:", number_input_c)
    print("원의 둘레: ", 2 * 3.14 * number_input_c)
    print("원의 넓이: ", 3.14 * number_input_c * number_input_c)

# finally 구문
# 예외 처리 구문에서 가장 마지막에 사용할 수 있는 구문
# try:
#   예외가 발생할 가능성이 있는 코드
# except:
#   예외가 발생했을 때 실행할 코드
# else :
#   예외가 발생하지 않았을 때 실행할 코드
# finally:
#   무조건 실행할 코드

try:
    number_input_d = int(input("정수 입력> "))
    print('finally까지..')
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름:", number_input_d)
    print("원의 둘레: ", 2 * 3.14 * number_input_d)
    print("원의 넓이: ", 3.14 * number_input_d * number_input_d)
finally:
    print("일단 프로그램 끝남")

# try, except, finally 구문의 조합
# 규칙
# try 구문은 단독으로 사용할 수 없으며 반드시 except 구문 또는 finally 구문과 함께 사용해야 한다.
# else 구문은 반드시 except 구문 뒤에 사용해야 한다.

# 파일이 제대로 닫혔는지 확인
try:
    file = open("info.txt", "w", encoding="UTF-8")
    file.close()
except Exception as e:
    print(e)

print("#파일이 제대로 닫혔는지 확인")
# print("file.closed:", file.closed)

# 파일 처리 중간에 예외 발생
try:
    file = open("info.txt", "w", encoding="UTF-8")
    
    # 예외 발생시킴
    예외.발생해라()
    
    file.close()
except Exception as e:
    print(e)

print("#파일이 제대로 닫혔는지 확인")
print("file.closed:", file.closed)

# # finally 구문 사용해 파일 닫기
# try:
#     file = open("info.txt", "w", encoding="UTF-8")
    
#     # 예외 발생시킴
#     예외.발생해라()
    
#     file.close()
# except Exception as e:
#     print(e)
# finally:
#     file.close()
# print("#파일이 제대로 닫혔는지 확인")
# print("file.closed:", file.closed)

#try 구문 내부에서 return 키워드를 사용하는 경우
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else :
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test()함수의 마지막 줄입니다.")

test()

# finally 키워드 활용
def write_text_file(filename, text):
    try:
        file = open(filename, "w", encoding="utf-8")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()

write_text_file("test.txt", "안녕하세요")

# 반복문과 함께 사용하는 경우

# 리스트 내부에서 특정값이 어디있는지 확인할때 index() 함수 사용
numbers = [52, 273, 273, 32, 100, 90, 10, 275]
print(numbers.index(52))
print(numbers.index(90))

# # 해당 값이 여러 개 있을 경우 첫 번째 값에 위치를 리턴한다.
print(numbers.index(273))

# # 리스트에 없는 값에 접근하려고 할 때 ValueError 예외가 발생

# 확인 문제2
# 조건문을 사용한 코드
# try except 구문을 사용한 코드
# 예외가 발생하지 않고 코드가 실행 결과처럼 출력되게 만들어라
num = [52, 273, 32, 103, 90, 10, 275]

print("# (1) 요소 내부에 있는 값 찾기")
print("- {}는 {} 위치에 있습니다.".format(52, num.index(52)))
print()

print("# (2) 요소 내부에 없는 값 찾기")
number = 1000000


try:
        print("- {}는 {} 위치에 있습니다.".format(52, num.index(number)))
except:
    print("리스트 내부에 없는 값입니다.")
print()
print("===정상 종료===")

