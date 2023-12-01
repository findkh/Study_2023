money = 2000
if money >= 3000:
    print("택시 타고 가")
else:
    print("걸어 가")

# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가 그렇지 않으면 걸어가
money = 3000
card = False
if money >= 3000 or card :
    print('택시타고가')
else:
    print('걸어가')

print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시 타')
else :
    print('걸어가')

# 주머니에 카드가 없다면 걸어가고, 있다면 버스 타고 가라 조건문으로 만들기
if 'card' not in pocket:
    print('걸어가라')
else:
    print('버스 타고 가라')

# 조건문에서 아무 일도 하지 않게 설정
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')

# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라
if 'money' in pocket:
    print('택시 타')
elif card:
    print('택시 타')
else:
    print('걸어가')

# if문을 한 줄로 작성하기
if 'money' in pocket: pass
else:print('카드를 꺼내라')

# 조건부 표현식
score = 75
if score >= 60:
    message = "success"
else:
    message = "failure"

print(message)

score = 30
message = "success" if score >= 60 else "failure"
print(message)