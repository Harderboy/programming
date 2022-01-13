import sys
 
def f1(str):
    global sports
    if str.upper() == "EXIT":
        sys.exit("User exit")
    else:
        sports.append(str)
 
# usrs = ['Lily', 'Hebe', 'Tom']
# for usr in usrs:
#     sports = []
#     print(usr + ", input your favorite sports and type exit to exit.")
#     while True:
#         response = input(": ")
#         try:
#             f1(response)
#         except SystemExit as msg:  # 捕捉异常，不退出程序，此处用来打印异常消息和退出while循环
#             print(msg)
#             print(usr + "'s favorite sports is " + ", ".join(i.lower() for i in sports) + '.')
#             break

# print(", ".join(("tall",)))
sports=["tall"]
print(type(i.lower() for i in sports))