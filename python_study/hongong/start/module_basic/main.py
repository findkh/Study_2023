# import test_module as test

# radius = test.number_input()
# print(test.get_circumference(radius))
# print(test.get_circle_area(radius))


# __name__="__main__"
# 프로그램의 진입점을 엔트리 포인트 또는 메인이라 부른다.
# 엔트리포인트 또는 메인 내부에서의 __name__은 "__main__"입니다.

# 모듈의 __name__
# 엔트리 포인트가 아니지만 엔트리 포인트 파일 내에서 import되면 모듈 내 코드가 실행된다.
# 모듈 내부에서 __name__을 출력하면 모듈의 이름을 나타낸다.

import test_module

print("# 메인의 __name__ 출력하기")
print(__name__)
print()