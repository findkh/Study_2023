# 외부 모듈을 사용하여 100~1000 사이에 있는 소수가 몇 개인지 구하기
# 소수는 영어로 Prime Number라고 부르며 1과 자기자신 외에는 어떠한 수로도 나누어 떨어지지 않는 수를 말한다.

from primePy import primes

count = 0
def getPrimeNumber(a, b):
    global count
    for i in range(a, b+1):
        if primes.check(i) == True:
            count += 1
    return count


result = getPrimeNumber(100, 1000)
print(count,"개")