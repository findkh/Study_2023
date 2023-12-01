# 함수 만들기
# 함수는 코드의 집합이다. 
# def 함수 이름():
#   문장

def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()

# def 함수이름(매개변수, 매개변수, ...)
#   문장

def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)

# 매개 변수와 TypeError
# 지정한 매개변수와 호출한 매개변수의 개수가 같지 않으면 오류가 발생한다.

# 가변 매개변수
# 가변 매개변수는 매개변수 개수가 변할 수 있다는 의미다.
# def 함수 이름(매개변수, 매개변수, ..., *가변 매개변수):
#   문장
# 제약 :
#   가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
#   가변 매개변수는 하나만 사용할 수 있다.
def print_2_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_2_times(3, "안녕하세요", "수달", "꼬꼬")

# 기본 매개변수
# 매개변수=값 형태
# 매개변수를 입력하지 않았을 경우 매개변수에 들어가는 기본값
# 제약 :
#   기본 매개변수 뒤에는 일반 매개변수가 올 수 없다.
def print_3_times(value, n=2):
    for i in range(n):
        print(value)

print_3_times("안녕하세요")

# 키워드 매개변수
# 기본 매개변수가 가변 매개변수보다 앞에 오면 -> 에러
# 가변 매개변수가 기본 매개변수보다 앞에 올 때 -> 가변 매개변수가 우선된다.
# 기본 매개변수와 가변 매개변수를 같이 사용하기 위해 키워드 매개변수가 있다
# print(value, ..., sep= ' ', end='\n', file=sys.stdout, flush=False)
def print_4_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_4_times("안녕하세요", "수달", "꼬꼬", n=3) #n=3이 키워드 매개변수

# 기본 매개변수 중에서 필요한 값만 입력하기
def test(a, b=10, c=100):
    print(a+b+c)

# 기본 형태
test(10, 20, 30)

# 키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10, b=100, c=200)

# 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10, a=100, b=200)

# 키워드 매개변수로 일부 매개변수만 지정한 형태
test(10, c=200)

# 리턴
# 자료 없이 리턴하기
# 함수 내부에서 return을 사용하면 함수를 실행했던 위치로 돌아가라는 뜻이다.
# 함수가 끝나는 위치를 의미한다.

def return_test():
    print("A 위치입니다.")
    return
    print("B 위치입니다.")

return_test()

# 자료와 함께 리턴하기
def return_test():
    return 100

value = return_test()
print(value)

# 아무것도 리턴하지 않기
def return_test2():
    return

value = return_test2()
print(return_test2())
# 파이썬은 None은 없다라는 의미다.

# 범위 내부의 정수를 모두 더하는 함수
def sum_all(start, end):
    output = 0
    for i in range(start, end+1):
        output += i
    return output

print(sum_all(0,100))


# 기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
def sum_all2(start=0, end=100, step=1):
    output = 0
    for i in range(start, end+1, step):
        output += i
    return output

print(sum_all2(0, 100, 10))
print(sum_all2(end=100))
print(sum_all2(end=100, step=2))

# 확인문제
# f(x)=2x+1
def f(x):
    return 2*x + 1
print(f(10))

# f(x)=x^+2x+1
def f2(x):
    return (x**2)+(2*x)+1
print(f2(10))

# 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수를 만들기
def mul(*values):
    total = 1
    for val in values:
        total *= val
    return total

print(mul(5,7,9,10))