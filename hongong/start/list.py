# 리스트 선언
# 대괄호에 자료를 쉼표로 구분하여 넣는다.
list_a = [273, "수달", 14, True, False]

# 리스트 접근 방법
# 1. 대괄호 안에 음수를 넣어 뒤에서부터 요소를 선택
print(list_a[0])
print(list_a[1])
print(list_a[3])
print(list_a[4])

# 2. 리스트 접근 연산자는 이중으로 사용할 수 있다.
print(list_a[1][0]) #수

# 3. 리스트안에서 리스트를 사용할 수 있다.
list_a = [[1,2,3],[4,5,6],[7,8,9]]
print(list_a[1])
print(list_a[1][2])

# 리스트 IndexError 예외
# => 리스트의 길이를 넘는 인덱스로 요소에 접근하려 할 때 발생

# 리스트 연산하기: 연결(+), 반복(*), len()
list_a = [1,2,3]
list_b = [4,5,6]

print("# 리스트 출력")
print("list_a =", list_a)
print("lisb_b", list_b)
print()

# 기본 연산자
print("list_a + list_b = ", list_a + list_b)
print("list_a * 3 = ", list_a * 3)
print()

# 함수
print("# 길이구하기")
print("len(list_a)", len(list_a))

# 리스트에 요소 추가하기: append(), insert()
# 리스트명.append(요소)
# 리스트명.insert(위치, 요소)

# 리스트에 요소 추가하기
list_a = [1,2,3]
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가하기
list_a.insert(0,10)
print(list_a)

# 한번에 여러 요소를 추가하고 싶을때는 extend() 사용
list_a.extend([7,8,9])
print(list_a)

# 연결 연산자를 사용하면 원본에 영향을 주지 않지만, append(), insert(), extend() 함수는 리스트에 직접적인 영향을 준다.

# 리스트에 요소 제거
# 인덱스로 제거하기 : del, pop()
# del 리스트명[인덱스]
# 리스트명.pop(인덱스)

list_a = [0,1,2,3,4,5,6,7,8,9]
print("#리스트 요소 제거")
# del 키워드
del list_a[0]
print("del list_a[0] : ", list_a)

# pop()
list_a.pop(1)
print("pop(1): ", list_a)

# del 키워드 범위 지정 삭제
print("범위 지정 삭제")
list_b = [1,2,3,4,5,6,7,8,9]
del list_b[3:6]
print(list_b)

list_c = [1,2,3,4,5,6,7,8,9]
del list_c[:3]
print(list_c)

list_d = [1,2,3,4,5,6,7,8,9]
del list_d[3:]
print(list_d)

# 리스트 슬라이싱
# 리스트에 : 연산자로 리스트 범위를 지정하여 여러 요소를 선택하는 것을 슬라이싱이라고 한다.
# 리스트[시작_인덱스:끝_인덱스:단계]
numbers = [1,2,3,4,5,6,7,8,9]
#print("numbers[0:5:2] : ", numbers[0:5:2]) #numbers[0:5:2] :  [1, 3, 5]
print("numbers[::-1] : ", numbers[::-1]) #numbers[::-1] :  [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 값으로 제거하기 : remove()
# 리스트.remove(값)
list_e = [1,2,1,2]
list_e.remove(2)
print(list_e)
# 값이 여러개 있어도 가장 먼저 발견되는 하나만 제거 한다.

# 모두 제거하기 : clear()
# 리스트.clear()
list_f = [1,2,3,4,5]
list_f.clear()
print(list_f)

# 리스트 정렬하기 : sort()
# 리스트.sort()
list_g = [52, 273, 103, 32, 275, 1, 7]
list_g.sort() #오름차순
print(list_g)
list_g.sort(reverse=True) #내림차순
print(list_g)

# 리스트 내부에 있는지 확인하기 in/not in 연산자
# 값 in 리스트
print(273 in list_g)
print(14 in list_g)
print(32 not in list_g)
print(11 not in list_g)

# for 반복문
# for 반복자 in 반복할 수 있는 것:
#   코드

for i in range(10):
    print("출력")

#for 반복문과 리스트
arr = [273, 14, 7, 2, 199]
for el in arr:
    print(el)

for char in "안녕하세요":
    print(char)

# 중첩 리스트와 중첩 반복문
# 반복문을 여러 겹 중첩해 사용하면 중첩 반복문이라 부른다.
# 2차원 리스트에 반복문 한번 사용하기
list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]
print(list_of_list)
for items in list_of_list:
    print(items)

for items in list_of_list:
    for item in items:
        print(items)

# 전개 연산자
# 리스트 앞에 * 기호를 사용하면 된다.
# 리스트 내부에서 사용하는 경우
a = [1,2,3,4]
b = [*a, *a]
print(b) #[1, 2, 3, 4, 1, 2, 3, 4]

# append()함수를 사용한 경우
a = [1,2,3,4]
a.append(5)
print(a) #a내용 변경

# 전개 연산자 사용
b = [1,2,3,4]
c = [*b, 5]
print(b) #b는 영향 받지 않는다.
print(c) #새로운 리스트가 만들어짐

# 함수 매개변수 위치에 사용하는 경우
a = [1,2,3,4]
print(a)

# 확인 문제
list = [0,1,2,3,4,5,6,7]
#list.extend(list)
#list.append(10)
#list.insert(3,0)
#list.remove(3)
list.pop(3)
print(list)

# 확인문제2
nums = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for num in nums:
    if num >= 100:
        print("-100 이상의 수 : ", num)

# 확인문제3
# 홀짝
for num in nums:
    if num % 2 == 0 :
        print("{} 는 짝수입니다.".format(num))
    else:
        print("{}는 홀수입니다.".format(num))

# 자리수
for num in nums:
    if((len(str(num)))==3):
        print("{}의 자리수는 {} 자릿수입니다.".format(num, (len(str(num)))))
    elif((len(str(num)))==2):
        print("{}의 자리수는 {} 자릿수입니다.".format(num, (len(str(num)))))
    else:
        print("{}의 자리수는 {} 자릿수입니다.".format(num, (len(str(num)))))

# 확인문제4
numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]

for number in numbers:
    output[(number-1)%3].append(number)
print(output)


for i in range(0, len(numbers) // 2):
    print(i)    
    j = numbers[int(i)+i]
    print(f"i = {i}, j = {j}")
    numbers[j] = numbers[j] ** 2

print(numbers)
