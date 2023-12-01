def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result

print(GuGu(2))

# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다 이들의 합은 23이다.
# 1000미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라

#. 1000미만의 자연수 구하기
for i in range (1, 1000):
    pass
    #print(i)

# 2. 3과 5의 배수 구하기
result = 0
for i in range (1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)

# 3. 게시판 페이징하기
# 함수 이름 : getTotalpage
# 입력 받는 값 : 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
# 출력하는 값 : 총 페이지 수
# -> 총 페이지 수 : (m/n)+1
def getTotalPage(m, n):
    return round((m/n)+1)
    
print(getTotalPage(5, 10))

# 4. 메모장 만들기
# 필요한 기능: 메모 추가하기, 메모 조회하기
# 입력받는 값: 메모 내용, 프로그램 실행 옵션
# 출력하는 값: memo.txt
# 입력 내용 : python memo.py -a "Life is too short"
# OK

# 5. 탭을 4개의 공백으로 바꾸기
# 필요한 기능 : 문서 읽어 들이기, 문자열 변경하기
# 입력 받는 값 : 탭을 포함한 문서 파일
# 출력 하는 값 : 탭이 공백으로 수정된 문서 파일
# 입력 내용 : python tabto4.py src dst
# OK

#6. 하위 디렉터리 검색하기
# 특정 디렉터리부터 시작해서 그 하위 모든 파일 중 파이썬 파일만 출력해주는 프로그램 작성
# OK
