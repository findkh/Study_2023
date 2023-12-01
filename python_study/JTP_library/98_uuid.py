# 98. uuid : 고유한 식별자 만들기

import uuid
 
# uuid1은 타임스탬프를 기준으로 생성하는 방식
a = uuid.uuid1()
print(a)

print(a.bytes)
print(a.hex)
print(a.int)

# uuid4는 랜덤 생성 방식
print(uuid.uuid4())