# # 1. 문자열 바꾸기
# # a:b:c:d를 a#b#c#d로 변경해라
# str = 'a:b:c:d'
# print(str.replace(':', '#'))

# # 2. 딕셔너리 값 추출하기
# # a 딕셔너리에 C에 해당하는 key 값이 없을 경우 오류 대신 70을 얻도록 수정해라
# a = {'A': 90, 'B': 80}
# print(a.get('C', 70))

# # 3. 리스트의 더하기와 extend 함수
# a = [1,2,3]
# # 리스트 a 에 [4,5]를 + 기호를 사용하여 더한 결과와 extend를 사용하여 더한 결과의 차이점에 대해 설명해라
# b = a
# print(b + [4, 5])
# print(b)

# c = a
# c.extend([4, 5])
# print(c)
# # -> +를 사용하면 원래 변수에 저장된 값이 변하는게 아니라 새로운 배열을 반환한다. 
# # -> extend는 주소값이 변하지 않는다.(원래 변수에 저장된 값도 변함)

# # 4. 리스트의 총합 구하기
# # 점수가 50점 이상인 점수의 총합을 구해라
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# result = 0

# for num in A:
#     if num >= 50:
#         result += num

# print(result)

# # 람다 사용
# print(sum(list(filter(lambda x: x >= 50, A))))

# # 5. 피보나치 함수
# # 입력을 정수 n으로 받았을 때 n 이하까지의 피보나치 수열을 출력하는 함수 작성
# def fib(n):
#     if n == 0 : return 0
#     if n == 1 : return 1
#     return fib(n-2) + fib(n-1)

# # for i in range(5):
# #     print(fib(i))

# inputNum = int(input('숫자 입력: >'))
# def fibo(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else :
#         result = fibo(num - 1) + fibo(num - 2)
#         return result

# print(fibo(inputNum))

# # 6. 숫자의 총합 구하기
# # 콤마로 구분된 숫자의 합을 구하는 프로그램 작성
# inputNum = input('숫자를 콤마로 구분하여 입력: >')
# inputList = inputNum.split(',')
# result = 0
# for i in inputList:
#     result += int(i)
# print(result)

# # 7. 한줄 구구단
# input = int(input('출력할 구구단 입력: >'))
# for i in range(1, 10):
#     print(i * input, end = ' ')

# # 8. abc.txt의 파일을 역순으로 바꾸어 저장
# with open("C:/Users/findk/git/python_study/JumpToPython/abc.txt", 'r') as f:
#     lines = f.readlines()

# lines.reverse()

# f = open('C:/Users/findk/git/python_study/JumpToPython/abc.txt', 'w')
# for line in lines:
#     line = line.strip()
#     f.write(line)
#     f.write('\n')
# f.close()

# # 9. 평균값 구하기
# with open('C:/Users/findk/git/python_study/JumpToPython/sample.txt', 'r') as f:
#     lines = f.readlines()

# f = open('C:/Users/findk/git/python_study/JumpToPython/result.txt', 'w')
# sum = 0

# for line in lines:
#     line = int(line.strip())
#     sum += line
# f.write(str(sum))
# f.write('\n')
# f.write(str(sum / len(lines)))
# f.close()

# 10. 사칙연산 계산기
class Calculator():
    def __init__(self, numberList):
        self.numberList = numberList
    
    def sum(self):
        result = 0
        for num in self.numberList:
            result += num
        return result

    def avg(self):
        total = self.sum()
        return total / len(self.numberList)

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())