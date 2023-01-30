from graphlib import TopologicalSorter

# 위상 정렬(topological sorting)
# 유향 그래프의 꼭짓점을 변의 방향을 거스르지 않도록 나열하는 것을 의미

ts = TopologicalSorter()

# 규칙1
ts.add('영어 중급', '영어 초급')
ts.add('영어 고급', '영어 중급')

# 규칙2
ts.add('영어 문법', '영어 중급')
ts.add('영어 고급', '영어 문법')

# 규칙3
ts.add('영어 회화', '영어 문법')

print(list(ts.static_order()))