import bisect

# 14. 점수에 따른 학점을 구하려면?
# bisect는 이진 탐색 알고리즘을 구현한 모듈로 bisect.bisect() 함수는 정렬된 리스트에 값을 삽입할 때 정렬을 유지할 수 있는 인덱스를 반환한다.

# 이상일 때
result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    pos = bisect.bisect([60, 70, 80, 90], score)
    grade = 'FDCBA'[pos]
    result.append(grade)

print(result)

# 기준을 초과로 변경할 때는 bisect_left() 함수 사용
result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    pos = bisect.bisect_left([60, 70, 80, 90], score)
    grade = 'FDCBA'[pos]
    result.append(grade)

print(result)

# bisect.insort() 함수는 정렬할 수 있는 위치에 항목을 삽입한다.
a = [60, 70, 80, 90]
bisect.insort(a, 85)
print(a)
