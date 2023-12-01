# mod1.py
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

if __name__ == "__main__":
    print(add(1,4))
    print(sub(4,2))

# print(add(1,4))
# print(sub(4,2))

# __name__ 변수
# 파이썬이 내부적으로 사용하는 특별한 변수 이름
# mod1.py 파일을 직접 실행할 경우 __name__ 변수에는 __main__값이 저장된다. 
# 하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import할 경우에는 mod1.py의 __name__변수에 mod1.py의 모듈 이름값이 저장된다.
