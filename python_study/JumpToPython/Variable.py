a = [1,2,3]
b = a
print(id(a))
print(id(b))

print (a is b) # a와 b가 가리키는 객체가 동일한가?

a[1] = 4
print(a)
print(b)

# 다른 주소를 가리키게 만들기 
# - [:] 사용
c = [1,2,3]
d = c[:]
c[1] = 4
print(c)
print(d)

# - copy 모듈 사용
from copy import copy
e = copy(c)
print(c)
print(e)
print(c is e)

# 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
print(a,b)
print([a,b])
a = b = 'python'
print(a, b)

a = 3
b = 5
a, b = b, a
print(a)
print(b)

a = [1,2,3]
b = [1,2,3]
print(a is b)
# a와 b 변수가 서로 다른 메모리이므로 false가 나온다.