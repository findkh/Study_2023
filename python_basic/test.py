str = 'python'

#index
print(str[2])
print(str[-1])

#slicing
print(str[2:4])

#split
str2 = '수달의 코딩 연습'
print(str2)
strs = str2.split()
print(strs)

#docstring
"""이것도 주석이지"""

#print 옵션
print("수달이짘ㅋ", end="//")

#escape code
print('\n')
print('수\n달')
print('\t 수 \t달')
print('수달', end='\t')
print('연습중')

#list
sudal_list = []
print(sudal_list)
print(type(sudal_list))

sudal_list = [1,2,3]
print(sudal_list)

std = []
print(std)
std.append('수달')
print(std)
std.append('고양이')
print(std)
std.append('닭')
std.append('호랑이')

print(std[3])
print(std[0:2])
del std[2]
print(std)

std.append('독수리')
std.append('뱀')
print(std)

std.sort()
print(std)

std.append('수달')
print(std)
print(std.count('수달'))

# Tuple
# 값 변경 불가
my_tuple = ()
print(my_tuple)
print(type(my_tuple))

my_tuple = 1, 2, 3
print(my_tuple)

#packing, unpacking
num1, num2, num3 = my_tuple
print(num1)
print(num2)
print(num3)

num1, num2 = num2, num1
print(num1)
print(num2)

# for문
for s in std:
    print(s)

for num in [1,2,3]:
    print(num)

for str in "수달의 코딩연습":
    print(str)

for n in range(0, 5):
    print(n)

print('========')
for n in range(5, 10):
    print(n)

for i in range(2,10):
    print('==구구단 {}단=='.format(i))
    for j in range(1,10):
        print('{} * {} = {}'.format(i, j, i*j))

# comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = []

for n in numbers:
    if n % 2 == 1:
        odd_numbers.append(n)

print(odd_numbers)

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)