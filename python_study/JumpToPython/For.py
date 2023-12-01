test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    print(mark)
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다" % number)
    else:
        print("%d번 학생은 불합격입니다" % number)

# continue문
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

# for 문과 range 함수를 사용하여 1부터 100까지 더하기
sumNumber = 0
for i in range(1, 101):
    sumNumber = sumNumber + i
print(sumNumber)

# for와 range를 사용한 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ')
    print(' ')

a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)
print(result)

# 리스트 내포 사용
result2 = [num * 3 for num in a]
print(result2)

result3 = [num * 3 for num in a if num % 2 == 0]
print(result3)