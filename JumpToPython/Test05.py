# 1. 아래의 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺼 수 있는 minus 메서드 추가
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        result = self
        self.value -= val
        return result

cal = UpgradeCalculator()
cal.add(10)

cal.minus(7)
print(cal.value)

# 2. 객체 변수 value가 100이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어라
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100 :
             self.value = 100
        else:
            self.value

cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)
print(cal2.value)

# 3. 결과를 예측
print(all([1,2,abs(-3)-3])) #False
print(chr(ord('a')) == 'a') #True

# 4. filter와 lambda를 사용하여 음수 제거
list_a = [1,-2,3,-5,8,-3]
# filter(조건 함수, 순회 가능한 데이터)
print(list(filter(lambda num : num > 0, list_a)))

# 5. 234(10)의 16진수를 구하고 10진수로 변환해라
print('16진수: ', hex(234))
print('10진수: ', int(hex(234), 16))

# 6. map과 lambda를 사용하여 다음 리스트를 각 요소값에 3이 곱해진 리스트를 만들어라
list_b = [1,2,3,4]
print(list(map(lambda num : num*3, list_b)))

# 7. 리스트의 최댓값과 최솟값을 구해라
list_c = [-8, 2, 7, 5, -3, 5, 0, 1]
print('최댓값: ', max(list_c))
print('최솟값: ', min(list_c))

# 8. 17/3의 결과의 소숫점 4자리까지만 반올림하여 표시해라
print(round(17 / 3, 4))

# 9. 다음과 같이 실행했을 때 입력값을 모두 더하는 myargv.py를 작성해라
# python myargv.py 1 2 3 4 5 6 7 8 10
# 결과 값 : 55
# 완료!

# 10. os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해라
# - 디렉토리로 이동한다.
# - dir 명령을 실행하고 그 결과를 변수에 담는다
# - dir 명령의 결과를 출력한다
# 완료!

# 11. glob 모듈을 사용하여 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해라
import glob
print(glob.glob("c:/Users/findk/git/python_study/JumpToPython/*.py"))

# 12. time 모듈을 사용하여 현재 날짜와 시간을 출력해라 : 2018/04/03 17:20:32
import time
print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time())))

# 13. random 모듈을 사용하여 로또 번호를 생성하라(중복 숫자가 있으면 안된다.)
import random

random_list = []
i=0
while len(random_list) != 6:
    randomNum = random.randint(1, 45)
    
    if randomNum not in random_list:
        random_list.append(randomNum)

print('로또번호: ', random_list)


