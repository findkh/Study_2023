# 집합 자료형
s1 = set([1,2,3])
print(s1)

s2 = set('Hello')
print(s2)

# 집합 자료형
# - 중복을 허용하지 않는다.
# - 순서가 없다
# 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만 set 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
# set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환한 후 해야 한다.

s1 = set([1,2,3])
l1 = list(s1) # 리스트로 변환
print(l1)

t1 = tuple(s1)
print(t1)

# 교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합
print(s1 & s2)

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))

# add : 값 1개 추가
s1 = set([1,2,3])
s1.add(4)
print(s1)

# update : 값 여러개 추가
s1.update([5,6,7])
print(s1)

# 특정 값 제거하기
s1.remove(3)
print(s1)
