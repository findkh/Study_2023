# 함수의 활용
# 재귀 함수
# 반복문으로 패하기
def factorial1(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output
print(factorial1(4)) 

# 재귀 함수로 팩토리얼 구하기
# 재귀란 자기 자신을 호출하는 것을 의미한다.
# factorial(n) = factorial(n-1) (n >= 1)
# factorial(0) = 1

def factorial2(n) :
    if n == 0:
        return 1
    else :
        return n * factorial2(n-1)

print(factorial2(1))
print(factorial2(2))
print(factorial2(3))
print(factorial2(4))

# 재귀 함수의 문제
# 피보나치 수열
def fibonacci(n):
    if n == 1 :
        return 1
    if n == 2 :
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("fibonacci(1) : ", fibonacci(1))
print("fibonacci(2) : ", fibonacci(2))
print("fibonacci(3) : ", fibonacci(3))
print("fibonacci(4) : ", fibonacci(4))

 # 재귀 함수로 구현한 피보나치 수열(2)
counter = 0
def fibonacci2(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter +=1

    if n == 1 :
        return 1
    if n == 2 :
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)

fibonacci2(10)
print("----")
print("fibonacci(10)에 활용된 덧셈 횟수는 {}번 입니다.".format(counter))

# 재귀 함수는 한 번 구했던 값이라도 처음부터 다시 계산 하기 때문에 계산 횟수가 기하급수적으로 늘어난다.
# global counter
# -> 파이썬은 함수 내부에서 함수 외부에 있는 변수를 참조하지 못한다.

dictinary = {
    1: 1,
    2: 1
}

def fibonacci3(n):
    if n in dictinary:
        # 메모가 되어 있으면 메모된 값을 리턴
        return dictinary[n]
    else :
        # 메모가 되어 있지 않으면 값을 구함
        output = fibonacci3(n-1) + fibonacci3(n-2)
        dictinary[n] = output
        return output
print("fibonacci3(10): ",fibonacci3(10))
print("fibonacci3(20): ",fibonacci3(20))
print("fibonacci3(30): ",fibonacci3(30))
print("fibonacci3(40): ",fibonacci3(40))

# 조기 리턴
# 흐름 중간에 return 키워드를 사용하는 것을 조기 리턴이라고 부른다.
def fibonacci4(n):
    if n in dictinary:
        return dictinary[n]
    output = fibonacci4(n-1) + fibonacci4(n-2)
    dictinary[n] = output
    return output

# 리스트 평탄화하는 재귀 함수 만들기
# -> 리스트 평탄화는 중첩된 리스트가 있을 때 중첩을 모두 제거하고 풀어서 1차원 리스트로 만드는 것을 의미한다.
def flatten(Data):
    output = []
    for item in Data:
        if(type(item) == list):
            output += item
        else:
            output.append(item)
    return output

example = [[1,[2,3]],4,[5,6],7,8,[9,10]]
print("원본", example)
print("평탄화: ", flatten(example))

def flatten2(Data):
    output = []
    for item in Data:
        if(type(item) == list):
            output += flatten2(item)
        else:
            output.append(item)
    return output

example = [[1,[2,3]],4,[5,6],7,8,[9,10]]
print("원본", example)
print("평탄화: ", flatten2(example))

# 확인문제1
# 여러 개의 테이블에 나누어 앉으려고 한다.
# 이떄 한 사람만 앉는 테이블이 없게 그룹을 지어야 한다.
# 한 개의 테이블에 앉을 수 있는 최대 사람의 수는 10명이다.
# 100명의 사람이 하나 이상의 테이블에 나누어 앉는 패턴을 구해라
memo = {}
def example(remainder, seated):
    key = str([remainder, seated])
    # 종료 조건
    if key in memo:
        return memo[key]

    if remainder < 0:
        return 0 # 무효하니 0을 리턴
    if remainder == 0:
        return 1 # 유효하니 수를 세면 되서 1을 리턴
    # 재귀 처리
    count = 0
    for i in range(seated, 10 + 1):
        count += example(remainder - i, i)
    # 메모화 처리
    memo[key] = count
    # 종료
    return count

print(example(100, 2))