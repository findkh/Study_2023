import time
# 시간
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
for i in range(10):
    print(i)
    time.sleep(1)

import calendar
# 달력
print(calendar.calendar(2023))
print(calendar.prcal(2022))
print(calendar.prmonth(2023,1))
print(calendar.weekday(2022,12,31)) # 월요일 0
print(calendar.monthrange(2023,3)) # 결과값: 1일이 무슨 요일인지, 며칠까지인지

import random
# 랜덤
print(random.random())
print(random.randint(1,10)) # 1~10사이 정수 중 난수값

def random_pop(data):
    number = random.randint(0, len(data) -1)
    return data.pop(number)

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data: print(random_pop(data))

import webbrowser
# webbrowser
webbrowser.open_new("http://google.com")

