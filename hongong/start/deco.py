# 함수 데코레이터
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper

@test
def hello():
    print("hello")

hello()

from functools import wraps

def test(function):
    @wraps(function)
    def wrapper(*arg, **kwargs):
        print("인사가 시작되었습니다.2")
        function(*arg, **kwargs)
        print("인사가 종료되었습니다.2")
    return wrapper

@test
def hello2():
    print("헬로2")

hello2()