# 에외 고급
# try:
#   예외가 발생할 가능성이 있는 구문
# except 예외의 종류 as 예외 객체를 활용할 변수 이름:
#   예외가 발생했을 때 실행할 구문

try:
    number_input_a = int(input("정수 입력>"))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    print("type(exception): ", type(exception))
    print("exception: ", exception)

# 여러 가지 예외가 발생할 수 있는 코드
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력>"))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)

# 예외 구분하기
# 파이썬은 except 구문 뒤에 예외의 종류를 입력해서 예외를 구분할 수 있다.

#ValueError와 IndexError 구분
list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input("정수 입력: >"))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력하세요")
except IndexError:
    print("리스트의 인덱스를 벗어났어요")

# 예외 구분 구문과 예외 객체
