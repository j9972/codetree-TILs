class Student:
    def __init__(self, kor, eng, math):
        self.k = kor
        self.e = eng
        self.m = math

a,b,c = tuple(input().split())
student1 = Student(a, b, int(c))
print("secret code :",student1.k) # 90
print("meeting point :",student1.e) # 80
print("time :",student1.m) # 90