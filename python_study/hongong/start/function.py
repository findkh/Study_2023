# 문자열, 리스트, 딕셔너리와 관련된 기본 함수
# 리스트에 적용할 수 있는 기본 함수 : min(), max(), sum()
numbers = [103, 52, 293, 32, 18]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# reversed() 함수
list_a = [1,2,3,4,5]
list_reversed = reversed(list_a)

print("# reversed() 함수")
print("reversed([1,2,3,4,5]):", reversed)
print("list(reversed([1,2,3,4,5])", list_reversed) #<list_reverseiterator object at 0x0000021A8300BE50>
print("list(reversed([1,2,3,4,5])):", list(list_reversed))
print()

print("for i in reversed([1,2,3,4,5]:")
for i in reversed(list_a):
    print("-", i)

# reversed() 함수의 결과가 제너레이터이기 때문에 첫 번째 반복문만 실행되고 두번 째 반복문은 실행되지 않는다.
temp = reversed([1,2,3,4,5,6])
for i in temp:
    print("첫 번째 반복문: {}".format(i))
for i in temp:
    print("두 번째 반복문: {}".format(i))

# 필요한 경우 for 구문 내부에 바로 넣어 사용한다.
for i in reversed([1,2,3,4,5,6]):
    print("두 번째 반복문: {}".format(i))
for i in reversed([1,2,3,4,5,6]):
    print("두 번째 반복문: {}".format(i))

# enumerate() 함수와 반복문 조합
example_list = ["요소A", "요소B", "요소C"]

print("# 단순 출력")
print(example_list)
print()

print("# enumberate() 함수 적용 출력")
print(enumerate(example_list))
print()

print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))

# 딕셔너리의 items() 함수와 반복문
example_dictionary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C",
}

print("# 딕셔너리의 items() 함수")
print("items(): ", example_dictionary.items())
print()

print("# 딕셔너리의 items() 함수와 반복문 조합하기")
for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))

# 리스트 내포
# 반복문을 사용한 리스트 생성
array = []
for i in range(0, 20, 2):
    array.append(i * i)
print(array)

# 리스트 안에 for 문 사용하기
array2 = [i * i for i in range(0, 20, 2)]
print(array2)

# 리스트 내포
# 리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것]
# 리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]

array3 = ["사과", "배", "감", "초콜릿", "귤", "바나나"]
output = [fruit for fruit in array3 if fruit != "초콜릿"]
print(output)

# 구문 내부에 여러 줄 문자열을 사용했을 때 문제점
number = int(input("정수 입력> "))

if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 짝수입니다.""".format(number, number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 홀수입니다.""".format(number, number))
# 인덱트가 들어감
number = int(input("정수 입력> "))

if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.
{}는(은) 짝수입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.
{}는(은) 홀수입니다.""".format(number, number))

number = int(input("정수 입력> "))
if number % 2 == 0:
    print("입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.".format(number, number))
else:
    print("입력한 문자열은 {}입니다.\n{}는(은) 홀수입니다.".format(number, number))

test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생략됩니다."
)
print("test: ", test)
print("type(test): ", type(test))

# 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결
number = int(input("정수 입력> "))
if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다."
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다."
    ).format(number, number))

# 문자열의 join() 함수
# 문자열.join(문자열로 구성된 리스트)
print("::".join(["1", "2", "3", "4", "5"]))

number = int(input("정수 입력> "))
if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다."
    ]).format(number, number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다."
    ]).format(number, number))

# reversed() 함수와 이터레이터
numbers = [1,2,3,4,5,6]
r_num = reversed(numbers)

# reversed_numbers를 출력
print("reversed_numbers :", r_num) #<list_reverseiterator object at 0x000001C8FF087C40>
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

# 이터레이터는 반복문을 매개변수로 전달할 수 있으며, next() 함수로 내부의 요소를 하나하나 꺼낼 수 있다.
# 리스트를 바로 리턴해주지 않고 이터레이터를 리턴해주는 이유
# => 메모리의 효율성, 리스트를 복제한 뒤 뒤집어서 리턴하는 것보다 기존 리스트를 활용해서 작업하는 것이 효율적이기 때문이다.

# 10진수와 2진수 변환
print("{:b}".format(10))
print(int("1010", 2))

# 10진수와 8진수 변환
print("{:o}".format(10))
print(int("12", 8))

# 10진수와 16진수 변환
print("{:x}".format(10))
print(int("10", 16))

print("안안안안녕하세요".count("안"))

# 확인 문제 2
# 1~100 사이에 있는 숫자 중 2진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고, 그 숫자들의 합을 구하는 코드(리스트 내포 사용)
output = [i for i in range(1, 101) if "{:b}".format(i).count("0") == 1 ]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계", sum(output))

# 숫자의 종류
# 리스트에서 몇 가지 종류의 숫자가 사용되었는지 구하는 프로그램
list1 = [1,2,3,4,1,2,3,3,2,1]
counter = {}

for i in list1:
    counter[i] = list1.count(i)


print(( "{}에서\n"
        "사용된 숫자의 종류는 {}개 입니다\n"
        "참고 : {}".format(list1, len(counter), counter)))


# 염기의 개수
# ctacaatgtcagtatacccattgcattagccgg
dnaList = input("염기 서열을 입력해주세요: >")
countList = {}

for i in dnaList:
    countList[i] = dnaList.count(i)

for key in countList :
    print("{}의 개수: {}".format(key, countList[key]))


# 염기 코돈 개수
codonStr = "ctacaatgtcagtatacccattgcattagccggc" #"ctaca"
codonList = []
codon = {}
preI = 0

for i in range(3,len(codonStr),3):
    codonList.append(codonStr[preI:i])
    preI = i

if (len(codonStr) % 3 != 0) :
    codonList.remove(codonList[len(codonList)-1])
    
for i in codonList:
    codon[i] = codonList.count(i)

print(codon)

# 2차원 리스트 평탄화
list = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
flatList = []

for i in range(0, len(list)):
    if type(list[i]) == int:
        flatList.append(list[i])
    else :
        for i in list[i]:
            flatList.append(i)

print(flatList)

    
