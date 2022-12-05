# 함수 고급
# 튜플 : 리스트와 비슷한 자료형, 한번 결정된 요소는 바꿀 수 없다.
tuple_test = (10, 20, 30)
print(tuple_test[0])
print(tuple_test[2])

# 요소를 하나만 가지는 튜플
print(type((273))) # <class 'int'>
print(type((273,))) # <class 'tuple'>

# 리스트와 튜플의 특이한 사용
# 리스트와 튜플 변수 할당
[a,b] = [10, 20]
(c,d) = (10, 20)
print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)

# 튜플은 괄호를 생략해도 튜플로 인식할 수 있는 경우 생략해도 된다.
# 괄호가 없는 튜플
tuple_test2 = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test2 : ", tuple_test2)
print("type(type_test2) : ", type(tuple_test2))
print()

# 괄호가 없는 튜플 활용
a, b, c = 10, 20, 30
print("# 괄호가 없는 튜플 활용")
print("a: ", a)
print("b: ", b)
print("c: ", c)

# 변수의 값을 교환하는 튜플
a, b = 10, 20
print("# 교환 전")
print("a: ", a)
print("b: ", b)

# 값 교환
a, b = b, a
print("# 교환 후 값")
print("a: ", a)
print("b: ", b)

# 튜플과 함수
# => 튜플은 함수의 리턴에 많이 사용한다.
def test():
    return (10, 20)

a, b = test()
print("a: ", a)
print("b: ", b)

# 튜플 리턴 예
for i, value in enumerate([1,2,3,4,5,6,7,8]):
    print("{}번째 요소는 {}입니다.".format(i, value))

a, b = 97, 30
print(a // b)

a, b = 97, 40
x, y = divmod(a, b)
print(x)
print(y)
