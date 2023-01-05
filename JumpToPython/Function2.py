# abs : 절대값을 돌려줌
print(abs(3.21))
print(abs(-3.21))

# all : 반복 가능한 자료형 x를 입력 인수로 받으며 x가 모두 참이면 True, 겆시이 하나라도 있으면 False를 돌려준다.
print(all([1,2,3])) #True
print(all([1,2,3,0])) #False

# any : x중 하나라도 참이 있으면 True를 돌려주고 x가 모두 거짓일 떄에만 False를 돌려준다. all의 반대다.
print(any([1,2,3,0])) #True
print(any([0,''])) #False

# chr : 아스키코드 값을 입력 받아 그 코드에 해당하는 문자를 출력하는 함수
print(chr(97))
print(chr(49))

# dir : 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다. 자료형 함수
print(dir([1,2,3]))
print(dir({'1':'a'}))

# divmod : 2개의 숫자를 입력 받고, a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려준다.
print(divmod(7, 3))

# enumerate : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval : 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 돌려주는 함수
print(eval('1+2'))
print(eval("'su' + 'dal'"))
print(eval('divmod(4,3)'))

# filter : 첫번째 인수는 함수이름, 두번쨰 인수는 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
#          두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서 돌려준다.
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
# 람다로 변환
print(list(filter(lambda x : x > 0, [1, -3, 2, 0, -5, 6])))

# hex : 정수값을 입력받아 16진수로 변환하여 돌려준다.
print(hex(124))
print(hex(3))

# id : 객체를 입력받아 객체의 고유 주소 값을 돌려주는 함수다.
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
print(id(4))

# input : 사용자 입력을 받는 함수다.
a = input('입력: >')
print(a)

# int : 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로 정수를 입력받으면 그대로 돌려준다.
print(int('3'))
print(int(3.4))

# int(x, radix) : radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.
print(int('11', 2))
print(int('1A', 16))

# isinstance : 첫번쨰 인수로는 인스턴스, 두번째 인수로는 클래스 이름을 받는다.
#              입력으로 받은 인스턴스가 그 클래스의 인스턴스인지 판단하여 참이면 True, 거짓이면 False를 리턴한다.
class Person : pass

a = Person()
b = 3
print(isinstance(a, Person))
print(isinstance(b, Person))

# len : 입력값의 길이, 요소의 전체 개수를 돌려주는 함수다.
print(len('python'))
print(len([1,2,3]))
print(len([1,'a']))

# list : 반복 가능한 자료형을 입력받아 리스트로 만들어 돌려주는 함수다.
print(list('python'))
print(list((1,2,3)))

# map : 함수와 반복 가능한 자료형을 입력 받는다.
#       입력 받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수다.
def two_times(x): return x*2

print(list(map(two_times, [1,2,3,4])))
# lambda
print(list(map(lambda a: a*2, [1,2,3,4])))

# max : 인수로 반복 가능한 자료형을 입력 받아 그 최대값을 돌려준다.
print(max([1,2,3]))

# min : 인수로 반복 가능한 자료형을 입력 받아 그 최소값을 돌려준다.
print(min([1,2,3]))

# oct : 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수다.
print(oct(34))
print(oct(12345))

# open(filename, [mode]) : 파일 이름과 읽기 방법을 입력 받아 파일 객체를 돌려주는 함수다. 읽기 방법을 생략하면 읽기(r)모드로 객체를 만들어 돌려준다.

# ord : 문자의 아스키 코드 값을 돌려주는 함수다.
print(ord('a'))
print(ord('0'))

# pow(x, y) : x의 y 제곱한 결과값을 돌려주는 함수다.
print(pow(2, 4))
print(pow(3, 3))

# range([start,] stop [,step]) : 주로 for문과 사용하는 함수로, 입력 받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))

# round(number[,ndigits]) : 숫자를 입력받아 반올림 해주는 함수
print(round(4.6))
print(round(4.2))
print(round(5.123456, 2)) # 소수점 2자리까지만 반올림하여 표시

# sorted(iterable) : 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수다
print(sorted([3,4,1]))
print(sorted(['a', 'd', 'b']))
print(sorted('zero'))
print(sorted((3, 2, 1)))

# str : 문자열 형태로 객체를 변환하여 돌려주는 함수다.
print(str(3))
print(str('hi'))
print(str('hi'.upper()))

# sum : 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수다.
print(sum([1,2,3]))
print(sum([4,5,6]))

# tuple : 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수다. 튜플이 입력으로 들어오면 그대로 돌려준다.
print(tuple('abc'))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

# type : 입력값의 자료형이 무엇인지 알려주는 함수
print(type('abc'))
print(type([]))
print(type(open("test.txt", 'r')))

# zip : 동일한 개수로 이루어진 자료형을 묶어 주는 역할
print(list(zip([1,2,3], [4,5,6])))
print(list(zip([1,2,3], [4,5,6], [7,8,9])))
print(list(zip('abc', 'def')))