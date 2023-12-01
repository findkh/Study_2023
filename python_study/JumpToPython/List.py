a = [1,2,3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[-1][0])

b = [1,2,3,['a', 'b', ['life', 'is', 'short']]]
print(b[-1][2][0])

A = [1,2,3,4,5] 
print(a[1:3])

# 중첩된 리스트에서 슬라이싱하기
c = [1,2,3,['a','b','c'],4,5]
print(c[2:5])
print(c[3][:2])

# 리스트 더하기
a = [1,2,3]
b = [4,5,6]
print(a+b)

# 리스트 반복하기
a = [1,2,3]
print(a * 3)

# 리스트 길이
print(len(a))

# 리스트 값 수정
a[2] = 4
print(a)

del a[1]
print(a)

a = [1,2,3,4,5]
del a[3:]
print(a)

# 요소 추가
a.append(4)
print(a)

a.append([1,3])
print(a)

# 리스트 정렬
a = [1,3,5,2]
a.sort()
print(a)

a = ['d', 'a', 'c', 'b']
a.sort()
print(a)

# 리스트 뒤집기
a = ['a', 'b', 'c', 'd']
a.reverse()
print(a)

# 위치 반환(index)
# index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.
# 존재하지 않는 값은 ValueError 발생
a = [1,2,3,4]
print(a.index(3))

# 리스트에 요소 삽입
a = [1,2,3]
a.insert(0,4)
print(a)

# 리스트 요소 제거
# remove(x) 리스트에서 첫번째로 나오는 x를 삭제
a = [1,2,3,1,2,3]
a.remove(3)
print(a)

# pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제
a = [1,2,3]
print(a.pop(1))
print(a)

# 리스트 확장
a = [1,2,3]
a.extend([4,5])
print(a)