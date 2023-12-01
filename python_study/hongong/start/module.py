# 표준 모듈
# 파이썬은 모듈이라는 기능을 활용해 코드를 분리하고 공유한다.
import math

# 사인
print(math.sin(1))
# 코사인
print(math.cos(1))
# 탄젠트
print(math.tan(1))
# 내림
print(math.floor(2.5))
# 올림
print(math.ceil(2.5))

# from 구문
# from 모듈 이름 import 가져오고 싶은 변수 또는 함수
from math import sin, cos, tan, floor, ceil
# 사인
print(sin(1))
# 코사인
print(cos(1))
# 탄젠트
print(tan(1))
# 내림
print(floor(2.5))
# 올림
print(ceil(2.5))

# as 구문
# import 모듈 as 사용하고 싶은 식별자
import math as m
# 사인
print(m.sin(1))
# 코사인
print(m.cos(1))
# 탄젠트
print(m.tan(1))
# 내림
print(m.floor(2.5))
# 올림
print(m.ceil(2.5))

# random 모듈
import random
print("# random 모듈")
# random():0.0 <= x < 1.0 사이의 float를 리턴한다.
print("- random(): ", random.random())

# uniform(min, max): 지정한 범위 사이의 float를 리턴한다.
print("- uniform(10, 20):", random.uniform(10, 20))

# randrange(): 지정한 범위의 int를 리턴한다.
# - randrange(max) : 0부터 max 사이의 값을 리턴한다.
# - randrange(min, max) : min부터 max 사이의 값을 리턴한다.
print("- choice([1,2,3,4,5]): ", random.randrange(10))

# choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택한다.
print("- choice([1,2,3,4,5]): ", random.choice([1,2,3,4,5]))

# shuffle(list) : 리스트의 요소들을 랜덤하게 섞는다.
print("- shuffle([1,2,3,4,5]): ", random.shuffle([1,2,3,4,5]))

# sample(list, k=<숫자>) : 리스트의 요소 중에 k개를 뽑는다.
print("- sample([1,2,3,4,5], k=2)", random.sample([1,2,3,4,5], k=2))

import os
print("현재 운영체제:", os.name)
print("현재 폴더: ", os.getcwd())
print("현재 폴더 내부의 요소: ", os.listdir)

# 폴더 만들고 제거하기
os.makedirs("hello")
os.rmdir("hello")

# 파일을 생성하고 파일 이름 변경
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# 파일 제거
os.remove("new.txt")

# 시스템 명령어 실행
os.system("dir")

# datetime 모듈
import datetime
# 현재 시각을 구하고 출력하기
print("# 현재 시각 출력")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

# 시간 출력
print("# 시간 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
# strftime()함수를 사용하면 시간을 형식에 맞춰 출력할 수 있으나, 한국어등의 문자는 매개변수에 넣을 수 없다.
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()

# 시간처리하기
print("# datetime.timedelta로 시간 더하기")

# 특정 시간 이후의 시간 구하기
# timedelta() 함수롤 사용하면 특정한 시간의 이전 또는 이후를 구할 수있다
# 다만 몇 년 후를 구하는 기능이 없으므로 replace를 사용해서 아예 날짜 값을 교체하는 것이 일반적이다.
after = now + datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

# 특정 시간 요소 교체하기
print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

# time 모듈
# 시간과 관련된 기능을 다룰 떄 사용한다.
# time.sleep()함수는 특정 시간 동안 코드 진행을 정지할 때 사용하는 함수다. 정지하고 싶은 시간을 초단위로 입력한다.
import time

print("지금부터 5초 동안 정지한다.")
time.sleep(5)
print("프로그램을 종료합니다.")

# urllib 모듈
# URL을 다루는 라이브러리다.
from urllib import request

#target = request.urlopen("https://google.com")
#output = target.read()

#print(output)

#operator.itemgetter() 함수
books = [
    {
        "title":"혼자 공부하는 파이썬",
        "price":18000
    },
    {
        "title":"혼자 공부하는 머신러닝 + 딥러닝",
        "price":26000
    },
    {
        "title":"혼자 공부하는 자바스크립트",
        "price":24000
    }       
]

def getPrice(book):
    return book["price"]

print(min(books, key=getPrice))
print(min(books, key=lambda book: book["price"]))

# operator 모듈의 itemgetter() 함수는 특정 요소를 추출하는 팜수를 만드는 함수다.
from operator import itemgetter

print("# 가장 저렴한책")
print(min(books, key=itemgetter("price")))
print()

print("# 가장 비싼 책")
print(max(books, key=itemgetter("price")))

 # 현재 디렉터리를 읽어 들이고 파일인지 디렉터리인지 구분하기
output = os.listdir(".")
print("os.listdir(): ", output)
print()

print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더: ", path)
    else:
        print("파일:", path)

# 폴더라면 또 탐색하기라는 재귀 구성으로 현재 폴더 내부에 있는 모든 파일을 탐색하도록 코드를 작성
def read_folder(path):
    print("=============={}=================".format(path))
    # 폴더의 요소 읽어 들이기
    folderItem = os.listdir(path)

    for item in folderItem:
        if os.path.isdir(item):
            print("폴더", item)
            read_folder(item)
        else:
            print("파일", item)

read_folder(".")