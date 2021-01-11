python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.count("Python"))

print("나는 %s색과 %s색을 좋아합니다" %("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아합니다.".format("빨강", "노랑"))
print("나는 {age}살이며, {color}색을 좋아합니다".format(age = 20, color = "빨간"))


addr = "http://google.com"
rmaddr = addr.replace("http://", "")
print(rmaddr)
rmdot = rmaddr[:rmaddr.index(".")]
print(rmdot)

answer = rmdot[:3] + str(len(rmdot)) + str(rmdot.count("e")) + "!"
print("생성된 비밀번호 : %s" %answer)

my_set = {1, 2, 3, 3, 3, 3}
print(my_set) 
# ---------------------------------------------------
from random import *

# users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(type(users))

users = range(1,21)
users = list(users)

shuffle(users)
print(users)

winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

#-----------------------------------------
