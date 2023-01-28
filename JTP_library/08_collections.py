from collections import deque

# 08. 앞뒤에서 자료를 넣고 빼기
# deque는 앞 뒤에서 데이터를 처리할 수 있는 양방향 자료형
# 스택처럼 써도 되고 큐처럼 써도 된다.

# 1~5가 적힌 다이얼이 있으며 현재 가리키는 눈금은 1이다. [1, 2, 3, 4, 5]
# 다이얼을 오른쪽으로 2칸 돌려 가리키는 눈금이 4가 되도록 만들어라. [4, 5, 1, 2, 3]
a = [1, 2, 3, 4, 5]
q = deque(a)
print(q)
q.rotate(3) # rotate : 시계방향 회전은 양수, 그 반대는 음수
result = list(q)
print(result)

print('===================')
q2 = deque(a)
print(q2)
q2.rotate(-2)
result2 = list(q2)
print(result2)

# list와 비슷한 deque
d = deque([1,2,3,4,5])
d.append(6)
print(d)
d.appendleft(0)
print(d)
print(d.pop())
print(d)
d.popleft()
print(d)

# 09. 자료에 이름 붙이기
from collections import namedtuple
data = [
    ('수달', 34, '010-1234-5678'),
    ('하파', 11, '010-2345-6789'),
    ('꼬꼬', 34, '010-3456-7890')
]

Employee = namedtuple('Employee', 'name, age, cellphone')

data = [Employee(emp[0], emp[1], emp[2]) for emp in data]
print(data)

data2 = [Employee._make(emp) for emp in data]
print(data2)

emp = data[0]
print(emp.name)
print(emp.age)
print(emp.cellphone)

# 키로 데이터 조회
print(emp._asdict)
print(emp[0])
print(emp[1])
print(emp[2])

new_emp = emp._replace(name="수달")
print(new_emp)

# 10. 사용한 단어 개수를 구하려면?
from collections import Counter
import re
data3 = """
산에는 꽃 피네
꽃이 피네
갈 봄 여름 없이
꽃이 피네

산에
산에
피는 꽃은
저만치 혼자서 피어 있네

산에서 우는 작은 새여
꽃이 좋아
산에서
사노라네

산에는 꽃 지네
꽃이 지네
갈 봄 여름 없이
꽃이 지네
"""

words = re.findall(r'\w+', data3)
print(words)
counter = Counter(words)
print(counter)
print(counter.most_common(1))
print(counter.most_common(3))

# 11. 딕셔너리를 한 번에 초기화하려면?
# collections.defaultdict는 값에 초기값을 지정하여 딕셔너리를 생성하는 모듈이다.
text = "Life is too Short, You need python"
d = dict()
for key in text:
    if key not in d:
        d[key] = 0
    d[key] += 1
print(d)


from collections import defaultdict
d = defaultdict(int)
for key in text:
    d[key] += 1
print(dict(d))