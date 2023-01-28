import heapq

# 12. 수상자 3명을 선정하려면?
# heapq는 순위가 가장 높은 자료를 가장 먼저 꺼내는 우선순위 큐를 구현한 모듈이다.
data = [
    (12.23, '강보람'),
    (12.31, '김지원'),
    (12.98, '박시우'),
    (11.99, '장준혁'),
    (11.67, '차정웅'),
    (12.02, '박중수'),
    (11.57, '차동현'),
    (12.04, '고미숙'),
    (11.97, '한시우'),
    (12.22, '이민석')
]

h = [] # 힙생성
for score in data:
    heapq.heappush(h, score)
    # print(heapq.heappush(h, score))

for i in range(3):
    print(heapq.heappop(h))

# heapify() 함수 사용
# data 리스트가 힙 구조에 맞게 변경된다.
print('=============heapify() 함수 사용============')
heapq.heapify(data)
for i in range(3):
    print(heapq.heappop(data))

# nsmallest() 함수 사용
print('=============nsmallest() 함수 사용============')
print(heapq.nsmallest(3, data))
print('=============nlargest() 함수 사용============')
print(heapq.nlargest(3, data))