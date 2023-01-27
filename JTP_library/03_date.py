import datetime

# 두 날짜의 차이 구하기
day1 = datetime.date(2020, 6, 14)
print(day1)
day2 = datetime.date(2023, 1, 7)
print(day2)

diff = day2 - day1
print(diff)
print(diff.days)

# datetime.datetime 객체
day3 = datetime.datetime(2022, 1, 27, 7 ,7, 39)
print(day3.hour)
print(day3.minute)
print(day3.second)

# datetime.date 객체와 datetime.time 객체를 합칠 때는 combine() 사용
day = datetime.date(2023, 1, 27)
time = datetime.time(7, 12, 12)
dt = datetime.datetime.combine(day, time)
print(dt)

# 요일 알아내기
# weekday : 0 월요일 
print(day.weekday())

# isoweekday : 1이 월요일
print(day.isoweekday())

# 오늘부터 사귀기로 한 커플의 100일은?
today = datetime.date.today()
print(today)

diff_days = datetime.timedelta(days=100)
print(diff_days)

day_100 = today + diff_days
print(day_100)