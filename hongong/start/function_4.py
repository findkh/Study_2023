# 제너레이터
# 제너레이터는 이터레이터를 직접 만들 때 사용하는 코드다.
# 함수 내부에 yield 키워드를 사용하면 해당 함수는 제너레이터함수가 되며, 일반 함수와 달리 함수 내부의 코드가 실행되지 않는다.
def test():
    print("함수가 호출되었습니다.")
    yield "test"

print("A 지점 통과")
test()

print("B 지점 통과")
test()
print(test()) #<generator object test at 0x000001204982A110>
# 제너레이터 함수는 제너레이터를 리턴한다.
# 제너레이터 객체는 next() 함수를 사용해 함수 내부의 코드를 실행한다.
# 이때 yield 키워드 부분까지만 살행하며, next() 함수의 리턴값으로 yield 키워드 뒤에 입력한 값이 출력된다.

# 제너레이터 객체와 next() 함수
def test2() :
    print("A지점 통과")
    yield 1
    print("B지점 통과")
    yield 2
    print("C지점 통과")

output = test()
# next() 함수를 호출
print("D지점 통과")
a = next(output)
print(a)
print("E지점 통과")
b = next(output)
print(b)
print("F지점 통과")
c = next(output)
print(c)
print(output)

# 리스트 함수의 key 키워드 매개변수
books = [{
    "title" : "혼자 공부하는 파이썬",
    "price" : 18000
}, {
    "title" : "혼자 공부하는 머신러닝 + 딥러닝",
    "price" : 26000
}, {
    "title" : "혼자 공부하는 자바스크립트",
    "price" : 24000
}]

def getPrice(book):
    return book["price"]

print("# 가장 저렴한 책")
print(min(books, key=getPrice))
print()

print("# 가장 비싼 책")
print(max(books, key=getPrice))

# 콜백 함수를 람다로 바꾸기
print("# 가장 저렴한 책")
print(min(books, key=lambda book: book["price"]))
print()

# print("# 가장 비싼 책")
print(max(books, key=lambda book: book["price"]))


# sort 함수로 오름차순 정리
a = [52, 273, 103, 32, 57, 272]
a.sort()
print(a)

# sort 내림 차순 
a.sort(reverse=True)
print(a)

# 딕셔너리 오름차순 정렬
print("# 가격 내림 차순")
books.sort(key=lambda book: book["price"], reverse=True)
for book in books:
    print(book)


#확인 문제 1
#1::2::3::4::5::6 만들기
numbers = [1,2,3,4,5,6]
print("::".join(map(str,numbers)))

# 확인 문제 2
numbers = list(range(1, 10+1))

print("# 홀수만 추출")
print(list(filter(lambda num : num % 2 != 0, numbers)))

print("# 3이상 7미만 추출")
print(list(filter(lambda num : num >= 3 and num < 7, numbers)))

print("# 제곱해서 50 미만 추출")
print(list(filter(lambda num : num*num < 50, numbers)))