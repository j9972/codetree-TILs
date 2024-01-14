class User:
    def __init__(self, code_name, color, second):
        self.code_name = code_name
        self.color = color
        self.second = second


# 변수 선언 및 입력
code_name, color, second = tuple(input().split())
u = User(code_name, color, int(second))
#print(u)
print("code : {}".format(u.code_name))
print("color : {}".format(u.color))
print("second : {}".format(u.second))