# 11. 모듈 사용 방법
# mymod.py 파이썬 모듈이 있다고 가정하고, 파이썬 셸을 열어 이 모듈을 import 해서 사용할 수 있는 방법을 모두 기술
# - 셸에서 mymod.py 가 있는 위치로 이동하여 import 한다
# - sys.path에 디렉토리를 추가한다.
# - 환경변수를 지정하여 사용한다

# 12. 다음 코드의 실행 결과를 예측하고 이유 설명
result = 0
try:
    [1,2,3][3]
    'a'+1
    4/0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)
# result = 0 + 3 + finally 4 
# 7

# 13. 숫자로 구성된 문자열을 입력받은 뒤,
# 문자열 안에서 홀수가 연속되면 두 수 사이에 -를 추가하고 짝수가 연속되면 *를 추가하는 기능을 가지고 있는  DashInsert 함수를 만들어라 

result = []
def DashInsert(n):
    nlist = list(map(int, str(n)))
    for i, num in enumerate(nlist):
        result.append(str(num))
        if i < len(nlist)-1:
            odd = num % 2 == 1
            nextOdd = nlist[i+1] % 2 == 1
            if odd and nextOdd:
                result.append('-')
            elif not odd and not nextOdd:
                result.append('*')
    print("".join(result))

DashInsert(4546793)

# 14. 문자열 압축하기
# 문자열을 입력 받아 같은 문자가 연속적으로 반복되는 경우 반복 횟수를 표시해 문자열을 압축하여 표시
inputStr = 'aaabbcccccca'
result = inputStr[0] 
count  = 0 

for st in inputStr:
    if st == result[-1]:
        count += 1
    else:
        result += str(count) + st
        count = 1
result += str(count)
print(result)

# 15. Duplicate Numbers
# 0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자가 한번씩 사용한 것인지 확인
def DuplicateNumbers(num):

    if len(num) != 10:
        return False
    
    numList = list(num)
    for i in range(0, 9):
        if str(i) not in numList: 
            return False
        else :
            return True

print(DuplicateNumbers('0123456789'))
print(DuplicateNumbers('01234'))
print(DuplicateNumbers('01234567890'))
print(DuplicateNumbers('6789012345'))
print(DuplicateNumbers('0123223456789'))

#16. 모스부호해독
mos = {'.-' : 'A', '-...': 'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H',
        '..' : 'I', '.---' : 'J', '-.-' : 'K', '.-..' : 'L', '--' : 'M', '-.' : 'N', '---' : 'O', '.--.' : 'P',
        '--.-' : 'Q', '.-.' : 'R', '...' : 'S', '-' : 'T', '..-' : 'U', '...-' : 'V', '.--' : 'W', '-..-' : 'X', '-.--' : 'Y', '--..' : 'Z'
    }

input = '... ..- -.. .- .-..  -.-. --- -.. .. -. --.'

result = []
for word in input.split('  '):
    for s in word.split(' '):
        result.append(mos[s])
    result.append(' ')

print(result)

# 17.a[.]{3,}b와 매치되는 문자열
import re
p = re.compile('a[.]{3,}b')
print(p.match('accb'))
print(p.match('a....b'))
print(p.match('aaab'))
print(p.match('a.ccb'))

# 18.
p = re.compile('[a-z]+')
m = p.search('5 python')
print(m.start() + m.end())

#19. 그루핑 -> 전화번호 뒷자리 ####로 변경
s = """
    park 010-9999-9988
    lee 010-1234-1234
    kim 010-1111-2222
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", s)
print(result)

#20. 전방탐색
pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("sudal@test.com"))