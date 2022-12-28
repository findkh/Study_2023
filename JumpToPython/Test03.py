# # 1. 코드의 결과 값 -> shirt
# a = "Life is too short, you nedd python"
# if "wife" in a :print("wife")
# elif "python" in a and "you" not in a: print("python")
# elif "shirt" not in a: print("shirt")
# elif "need" in a: print("need")
# else: print("none")

# # 2. while 문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합
# result = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         result += i
#     i += 1
# print(result)

# # 3. while문을 사용하여 별 표시하는 프로그램
# i = 0
# while True:
#     i += 1
#     if i > 5: break
#     print("*"* i)

# # 4. for문을 사용하여 1부터 100까지 숫자 출력
# for i in range(1,101):
#     print(i)

# 5. 중간고사 점수 평균 출력
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

# 6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 코드를 리스트 내포를 사용하여 표현
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
print(result)

# 리스트 내포로 표현
result = [num * 2 for num in numbers if num % 2 == 1]
print(result)