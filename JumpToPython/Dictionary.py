# 딕셔너리

# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'sudal'
print(a)
a[3] = [1,2,3]
print(a)

# 딕셔너리 요소 삭제
del a[1]
print(a)

# 딕셔너리에서 Key를 사용해 Value 얻기
grade = {'pey' : 10, 'julliet':99}
print(grade['pey'])
print(grade['julliet'])

# 딕셔너리 주의 사항
# - key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다.
a = {1: 'a', 1: 'b'}
print(a)
# - Key에는 리스트를 쓸 수 없다. 하지만 튜플은 Key로 쓸 수 있다.

# 키 리스트 만들기(keys)
a = {'name': 'sudal', 'phone': '01012345678', 'birth':'0112'}
print(a.keys())

for k in a.keys():
    print(k)

# value 리스트 만들기
print(a.values())

# key, value 쌍 얻기(items)
print(a.items())

# Key:Value 쌍 모두 지우기
a.clear()
print(a)

a = {'name': 'sudal', 'phone': '01012345678', 'birth':'0112'}
print(a.get('name'))
print(a.get('phone'))
print(a.get('nokey'))

# 딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때엔느 get(x, '디폴트값')
print(a.get('foo', 'bar'))

# key가 딕셔너리 안에 있는지 조사하기 -> in
print('name' in a)
print('email' in a)

dictionaryA = {'name' : '홍길동', 'birth':1234, 'age':30}
print(dictionaryA)
