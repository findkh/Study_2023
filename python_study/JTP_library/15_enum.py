from datetime import date

# enum은 서로 관련이 있는 여러 개의 상수 집합을 정의할 때 사용하는 모듈이다.

def get_menu(input_date):
    weekday = input_date.isoweekday()
    if weekday == 1:
        menu = '김치찌개'
    elif weekday == 2:
        menu = '비빔밥'
    elif weekday == 3:
        menu = '된장찌개'
    elif weekday == 4:
        menu = '불고기'
    elif weekday == 5:
        menu = '갈비탕'
    elif weekday == 6:
        menu = '라면'
    elif weekday == 7:
        menu = '건빵'
    return menu

print(get_menu(date(2021, 12, 6)))
print(get_menu(date(2021, 12, 18)))

# 매직 넘버 : 프로그래밍에서 상수로 선언하지 않은 숫자를 매직 넘버라 한다.
from enum import IntEnum

class Week(IntEnum):
    MONDAY = 1
    THESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_menu(input_date):
    menu = {
        Week.MONDAY : '김치찌개',
        Week.THESDAY : '비빔밥',
        Week.THURSDAY : '된장찌개',
        Week.THURSDAY : '불고기',
        Week.FRIDAY : '갈비탕',
        Week.SATURDAY : '라면',
        Week.SUNDAY : '건빵',
    }
    return menu[input_date.isoweekday()]

print(get_menu(date(2021, 12, 6)))
print(get_menu(date(2021, 12, 18)))

for week in Week:
    print("{}:{}".format(week.name, week.value))