from fractions import Fraction

# fractions는 유리수를 계산할 떄 사용하는 모듈이다.

print(1/5 + 2/5)

# 유리수는 Fraction(분자, 분모) 형태로 만들 수 있다.
a = Fraction(1, 5)
print(a)

# Fraction('분자/분모')처럼 문자열로 만들 수도 있다.
b = Fraction('1/5')
print(b)

# 분자 값은 numberator로 분모 값은 denominator로 알 수 있다.
print(a.numerator)
print(a.denominator)

# 1/5 + 2/5 = 3/5 계산
result = Fraction(1, 5) + Fraction(2, 5)
print(result)

# 실수로 변경
print(float(result))