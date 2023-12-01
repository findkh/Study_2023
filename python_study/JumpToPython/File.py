# 파일 생성하기
# 파일 객체 = open(파일 이름, 파일 열기 모드)
f = open("새파일.txt", 'w')
f.close()

# 파일 열기 모드
# r : 읽기
# w : 쓰기 
# a : 추가

# 위치 지정
f = open("C:/Users/findk/git/python_study/JumpToPython/newFIle.txt", 'w')
f.close()

# 파일을 쓰기 모드로 열어 출력값 적기
f = open('C:/Users/findk/git/python_study/JumpToPython/newFIle.txt', 'w', encoding='UTF-8')
for i in range(1, 11):
    data = '%d번째 줄입니다. \n' % i
    f.write(data)
f.close()

# 프로그램 외부에 저장된 파일을 읽는 방법
# 1. readline 함수 사용
f = open('C:/Users/findk/git/python_study/JumpToPython/newFIle.txt', 'r', encoding='UTF-8')
line = f.readline()
print(line)
f.close

# 모든 줄 읽기
f = open('C:/Users/findk/git/python_study/JumpToPython/newFIle.txt', 'r', encoding='UTF-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 2. readlines 함수 사용
f = open('C:/Users/findk/git/python_study/JumpToPython/newFIle.txt', 'r', encoding='UTF-8')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# 3. read 함수 사용
f = open('C:/Users/findk/git/python_study/JumpToPython/newFIle.txt', 'r', encoding='UTF-8')
data = f.read()
print(data)
f.close()

# 파일에 새로운 내용 추가하기
f = open('C:/Users/findk/git/python_study/JumpToPython/newFIle.txt', 'a', encoding='UTF-8')
for i in range(11, 20):
    data = "%d 번쨰 줄입니다.\n" % i
    f.write(data)
f.close()