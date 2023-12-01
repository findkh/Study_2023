import itertools

# 23. 상담원을 순서대로 배정
# itertools.cycle(iterable)은 반복 가능한 객체를 순서대로 무한히 반복하는 이터레이터를 생성하는 함수다.

emp_pool = itertools.cycle(['김은경', '이명자', '이성진'])


for i in range(0, 10):
    print(next(emp_pool))

# 24. 연간 매출약 계산
# itertools.accumulate(iterable)은 반복 가능한 객체의 누적합을 계산하여 이터레이터로 반환하는 함수다.
monthly_income = [1161, 1814, 1270, 2256, 1413, 1842, 2221, 2207, 2450, 2823, 2540, 2134]
result = list(itertools.accumulate(monthly_income))
print(result)

# 최댓값 표시하기
max_result = list(itertools.accumulate(monthly_income, max))
print(max_result)

# 25. 키 값으로 데이터를 묶기
import operator
import pprint

data = [
    {'name': '이민서', 'blood': 'O'},
    {'name': '이영순', 'blood': 'B'},
    {'name': '이상호', 'blood': 'AB'},
    {'name': '김지민', 'blood': 'B'},
    {'name': '최상현', 'blood': 'AB'},
    {'name': '김지아', 'blood': 'A'},
    {'name': '손우진', 'blood': 'A'},
    {'name': '박은주', 'blood': 'A'}
]
data = sorted(data, key=operator.itemgetter('blood'))
pprint.pprint(data)

grouped_data = itertools.groupby(data, key=operator.itemgetter('blood'))
result = {}
for key, group_data in grouped_data:
    result[key] = list(group_data)

pprint.pprint(result)

# 26. 부족한 것을 채워 묶으려면
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
rewards = ['사탕', '초컬릿', '젤리']

result = itertools.zip_longest(students, rewards, fillvalue='새우깡')
print(list(result))

# 27. 순서를 생각하며 카드를 뽑으려면
# itertools.permutations(iterable, r=None)은 반복 가능 객체 중에서 r개를 선택한 순열을 반환하는 함수다.
print(list(itertools.permutations(['1', '2', '3'], 2)))

for a, b in itertools.permutations(['1', '2', '3'],2):
    print(a,b)

# 28. 로또의 모든 가짓수를 구하려면?
# itertools.combinations(iterable, r)은 반복 가능한 객체 중에서 r개를 선택한 조합을 이터레이터로 반환하는 함수이다.
it = itertools.combinations(range(1, 45), 6)
# for num in it:
#     print(num)

print(len(list(itertools.combinations(range(1,46),6))))