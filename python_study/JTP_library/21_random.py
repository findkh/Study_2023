import random

# random은 난수를 생성할때 사용하는 모듈
result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)
print(result)

# 리스트 요소 무작위로 섞을 때
a = [1,2,3,4,5]
random.shuffle(a)
print(a)

# 리스트 요소에서 무작위로 하나를 선택하려면 random.choice()
print(random.choice(a))
