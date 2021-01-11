# python = "Python is Amazing"

# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("n"))
# print(python.count("Python"))

# print("나는 %s색과 %s색을 좋아합니다" %("파랑", "빨강"))
# print("나는 {1}색과 {0}색을 좋아합니다.".format("빨강", "노랑"))
# print("나는 {age}살이며, {color}색을 좋아합니다".format(age = 20, color = "빨간"))


# addr = "http://google.com"
# rmaddr = addr.replace("http://", "")
# print(rmaddr)
# rmdot = rmaddr[:rmaddr.index(".")]
# print(rmdot)

# answer = rmdot[:3] + str(len(rmdot)) + str(rmdot.count("e")) + "!"
# print("생성된 비밀번호 : %s" %answer)

# my_set = {1, 2, 3, 3, 3, 3}
# print(my_set) 
# ---------------------------------------------------
# 퀴즈 4
# from random import *

# # users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# # print(type(users))

# users = range(1,21)
# users = list(users)

# shuffle(users)
# print(users)

# winners = sample(users, 4)

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")

# ---------------------------------------------------
# 6-1 if

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈": 
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")


# temp = int(input ("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:                #이렇게 and 없이 바로 사용 가능
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")


# ---------------------------------------------------
# 6-2 for

# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1, 6):  # 1, 2, 3, 4, 5
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# ---------------------------------------------------
# 6-3 while

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}".format(customer, index))
#     index += 1
# 무한루프

# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")


# ---------------------------------------------------
# 6-4 continue와 break

# absent = [2, 5] # 결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# ---------------------------------------------------
# 6-5 한 줄 for

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]    # students에 있는 i(반복변수)들을 하나씩 불어오면서 거기에 100을 더한 값을 list로 바꿔서 students에 넣어라
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]   # students에 있는 i(반복변수)들을 하나씩 불러오면서 그 길이를 students에 넣어라
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students] 
# print(students)

# ---------------------------------------------------
# 퀴즈 5
from random import *
cnt = 0             # 총 탑승 승객 수

for i in range(1, 51):          # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 51)     # 5분 ~ 50분 소요 시간. (임의의 값 1개 생성)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분".format())
