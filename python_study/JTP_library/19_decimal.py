import math
from decimal import Decimal
# decimal.Decimal은 숫자를 10진수로 처리하여 정확한 소수점 자릿수를 표현할 때 사용하는 모듈이다.

print(0.1 * 3 == 0.3)
print(1.2 - 0.1 == 1.1)
print(0.1 * 0.1 == 0.01)

print(0.1 * 3)
print(1.2 - 0.1)
print(0.1 * 0.1)
# -> float 연산은 오차가 발생할 수 있다.

# == 연산자 대신 두 값이 가까운지를 확인하는 math.isclose() 함수 사용
print(math.isclose(0.1 * 3, 0.3))
print(math.isclose(1.2 - 0.1, 1.1))
print(math.isclose(0.1 * 0.1, 0.01))

# 십진수 연산을 사용하는 decimal.Decimal을 사용하여 문제를 해결
print(Decimal('0.1') * 3)
print(Decimal('1.2') - Decimal('0.1'))
print(Decimal('0.1') * Decimal('0.1'))

# decimal 자료형은 다시 float 자료형으로 형변환 할 수 있다.
print(Decimal('1.2') - Decimal('0.1')) == 1.1

# Decimal 사용시 문자열 '1.1' 대신 실수형 1.1을 입력하면 float연산에서 발생한 문제가 그대로 나타난다.

# Decimal은 정확성을 향상하고자 고정 소수점을 사용하여 메모리를 많이 차지한다.
# 금융권 또는 재무/회계 관련 프로그램을 작성할 때 사용하는 것이 좋다.