# 숫자형
print('14 / 3 = 몫: {}, 나머지: {}'.format(14//3, 14 %3))

# 문자형
# 문자열 만드는 방법
# 1. 큰따옴표로 양쪽 둘러싸기
# 2. 작은따옴표로 양쪽 둘러싸기
# 3. 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
# 4. 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기

# 문자열 안에 작은 따옴표 포함시키고 싶을 때
food = "Python's favorite food is perl."
print(food)

# 문자열에 큰따옴표 포함시키기
say = '"Python is very easy." he says.'
print(say)

# 백슬래시를 사용해서 작은따옴표와 큰따옴표 문자열에 포함시키기
food = 'python\'s favorite food is perl.'
say = "\"Python is very easy.\" he says."
print(food)
print(say)

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# - 이스케이프 코드 '\n' 삽입하기
multiline = "Life is too short\nYou need python"
print(multiline)

# - 연속된 작은따옴표3개 또는 큰 따옴표 3개 사용하기
multiline2 = '''
Life is too short
You need python
'''
print(multiline2)

multiline3 = """
Life is too short
You need python
"""
print(multiline3)

# 문자열 연산하기
# 1. 문자열 더해서 연결하기
head = "Python "
tail = "is fun!"
print(head + tail)

# 2. 문자열 곱하기
a = "python"
print(a * 2)

# 3. 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

# 4. 문자열 길이 구하기
str = 'You need python'
print(len(str))

# 문자열 인덱싱과 슬라이싱
# 파이썬은 0부터 숫자를 센다.
a = "Life is too short, You need Python"
print(a[0])
print(a[12])
print(a[-1])

# 문자열 슬라이싱
b = a[0] + a[1] + a[2] + a[3]
c = a[0:4] # 변수[시작인덱스:종료인덱스+1]
print(b)
print(c)
print(a[0:])
print(a[:])

# 슬라이싱으로 문자열 나누기
d = "20010331Rainy"
date = d[:8]
weather = d[8:]
print(date)
print(weather)

# 문자열 바꾸기
# 문자열은 immutable한 자료형이기 때문에 요소값을 바꿀 수 없다.
e = "Pithon"
print(e[:1] + 'y' + e[2:])

# 문자열 포매팅
print('I eat %d apples.' %3)
print('I eat %s apples.' % 'five')

number = 3
print('I eat %d apples.' %number)

# 2개 이상의 값 넣기
number = 10
day = "tree"
print('I ate %d apples. so I was sick for %s days.' %(number, day))

# 포매팅 연산자와 %d와 %를 같이 쓸 때는 %%를 사용한다.
print('Error is %d%%.' %98)

# 포맷 코드와 숫자 함께 사용하기
# 정렬과 공백
print('%10s' % 'hi')
print('%-10s' % 'hi')

# 소수점
print('%0.4f' % 3.42134234)
print('%10.4f' % 3.42134234)

# format 함수 사용
# 왼쪽 정렬
print('{0:<10}'.format('hi'))
# 오른쪽 정렬
print('{0:>10}'.format('hi'))
# 가운데 정렬
print('{0:^10}'.format('hi'))
# 공백 채우기
print('{0:=^10}'.format('hi'))
# 소수점 표현
y=3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
# {또는} 문자 표현
print('{{and}}'.format())

print('{0:!^12}'.format('python'))

# 문자 개수 세기
a = "hobby"
print(a.count('b'))

# 위치 알려주기
a = 'Python is the best choice'
print(a.find('b'))
print(a.find('k')) # 존재하지 않으면 -1
print(a.index('b'))
#print(a.index('k')) # ValueError: substring not found

# 문자열 삽입
print(','.join('abcd'))

# 소문자를 대문자로 
print('hi'.upper())

# 대문자를 소문자로
print('HI'.lower())

# 왼쪽 공백 지우기
print('     hi!!!!'.lstrip())

# 오른쪽 공백 지우기
print('hi!!!            '.rstrip())

# 양쪽 공백 지우기
print('    hi!!!     '.strip())

# 문자열 바꾸기
a = 'Life is too short'
print(a.replace('Life', 'Your leg'))

# 문자열 나누기
print(a.split())
b = "a:b:c:d"
print(b.split(':'))