# 딕셔너리는 키를 기반으로 값을 저장한다.
# 딕셔너리 선언하기
# => 딕셔너리는 중괄호로 선언하며 키ㅓ 만든다.
dict_a = {
    "name" : "어벤저스 엔드게임",
    "type" : "히어로 무비"
}
print(dict_a)
print(dict_a["name"])
print(dict_a["type"])

dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

print("name: ", dictionary["name"])
print("type: ", dictionary["type"])
print("ingredient", dictionary["ingredient"])
print("origin: ", dictionary["origin"])
print()

# 값 변경
dictionary["name"] = "8D 건조 망고"
print("name: ", dictionary["name"])

# 딕셔너리에 값 추가하기/제거하기
# 딕셔너리[새로운키] = 새로운 값
dictionary["price"] = 5000
print(dictionary)

# 이미 존재하는 키를 지정하고 값을 넣으면 새로운 값으로 대치된다.
dictionary["name"] = "9D 건조 망고"
print(dictionary)

# del 키워드 : 삭제
del dictionary["ingredient"]
print(dictionary)

# 딕셔너리 선언
dictionary = {}
print("요소 추가 전: ", dictionary)

dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"
print("요소 추가 이후: ", dictionary)

# 딕셔너리 요소 제거
dictionary = {
    "name" : "수달",
    "job" : "Full Stack Developer"
}
print("요소 제거 이전: ", dictionary)

del dictionary["name"]
del dictionary["job"]
print("요소 제거 후: ", dictionary)

# KeyError 예외
# => 존재하지 않느 키에 접근하면 KeyError 발생

# 딕셔너리 내부에 키가 있는지 확인
# in 키워드
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : "",
    "origin" : "필리핀"
}

dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}
key = input("> 접근하고자 하는 키 : ")

if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

# get() 함수
# => 딕셔너리의 키로 값을 추출하는 기능, 존재하지 않는 키에 접근할 경우 None을 출력한다.
value = dictionary.get("존재하지 않는 키")
print("값: ", value)
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")

# for 반복문: 딕셔너리와 함께 사용
# for 키 변수 in 딕셔너리:
#   코드
for key in dictionary:
    print(key, ":", dictionary[key])

# 확인문제1
dict_a = {}
dict_a["name"] = "구름"
print(dict_a)

del dict_a["name"]
print(dict_a)

# 확인문제2
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "하파", "age": 10},
    {"name": "호랑이", "age": 4}
]

print("# 우리 동네 애완 동물들")
for pet in pets:
    print("{} {}살".format(pet["name"], pet["age"]))

# 확인문제 3
numbers = [1,2,6,8,3,9,2,3,5,6,8,7,9,1,4,3,2,1,5,4,7,8,2,3,2,3,1,3]
counter = {}

for number in numbers:
    counter[number] = numbers.count(number)

print(counter)

# 확인문제 4
character = {
    "name": "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아줘 세게 베기"]
}

for key in character:
    if (type(character[key]) is str) :
        print("{} : {}".format(key, (character[key])))
    if (type(character[key]) is int) :
        print("{} : {}".format(key, (character[key])))
    if (type(character[key]) is list) :
        for item in character[key]:
            print("{} : {}".format(key, item))
    if (type(character[key]) is dict) :
        dict_a = character[key]
        for key in dict_a:
            print("{} : {}".format(key, dict_a[key]))

