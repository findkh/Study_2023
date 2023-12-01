# 여러개의 입력값을 받는 함수
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul', 1,2,3,4,5)
print(result)

# 키워드 파라미터
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)
# 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결과값이 그 딕셔너리에 저장된다.

# return 쓰임새
# -> return을 단독으로 써서 함수를 빠져나갈 수 있다.
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)

say_nick('야호')
say_nick('바보')

# 매개변수에 초기값 미리 설정
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응용", 27, False)

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# global 명령어 사용
a = 1
def vartest2():
    global a
    a = a + 1
vartest2()
print(a)

# lambda
# lambda 매개변수1, 매개변수2, ... : 매개변수를 사용한 표현식
add = lambda a, b: a + b
result = add(3, 4)
print(result)