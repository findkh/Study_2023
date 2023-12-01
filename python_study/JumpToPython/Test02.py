# 1. 홍길동의 평균 점수
# 방법1
score = [50, 75, 55]
print(sum(score) / len(score))

# 방법2
total = 0
for num in score:
    total += num
print(total/ len(score))

# 2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법
num = 13
if(num / 13 == 0):
    print('짝수')
else:
    print('홀수')

# 3. 홍길동의 주민번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력
pin = "881120-1068234"
yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]
print(yyyymmdd)
print(num)

# 4. 주민번호 뒷자리의 맨 첫번째 숫자로 성별을 나타내는 숫자를 출력
print(num[0:1])

# 5. replace 함수를 사용하여 a#b#c#d로 바꿔서 출력
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

# 6. [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들기
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# 7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

# 8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4) 만들기
a = (1,2,3)
a = a+(4,)
print(a)

# 9. 오류 발생 이유
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python' # 딕셔너리의 키는 변하는 값을 사용할 수 없다.
a[250] = 'python'
print(a)

# 10. 딕셔너리 a에서 B에 해당하는 값 추출
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

# 11. a 리스트에서 중복 숫자를 제거
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

# 12. 다음과 같은 결과가 나오는 이유를 설명
a = b = [1,2,3]
a[1] = 4
print(b)
# a와 b의 메모리 주소가 같기 때문