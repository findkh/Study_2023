import calendar

# 윤년 확인
# 1. 서력 기원 연수가 4로 나누어 떨어지는 해는 윤년
# 2. 그중에서 100으로 나누어 떨어지는 해는 평년
# 3. 400으로 나누어 떨어지는 해는 다시 윤년

def is_leap_year(year):
    if year % 4 == 0:
        return True
    if year % 100 == 0:
        return False    
    if year % 400 == 0:
        return True
    return False

print(is_leap_year(2019))
print(is_leap_year(2020))

print(calendar.isleap(1))
print(calendar.isleap(4))
print(calendar.isleap(2019))
print(calendar.isleap(2020))