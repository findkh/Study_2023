class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value

    def __str__(self):
        return self.message

    def print(self):
        print("### 오류 정보 ####")
        print("메세지:", self.message)
        print("값:", self.value)

try:
    raise CustomException("그냥 오류", 273)
except CustomException as e :
    e.print()