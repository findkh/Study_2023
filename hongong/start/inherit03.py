class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("#### 내가 만든 오류 생성 ####")
    def __str__(self):
        return "오류 발생"

raise CustomException