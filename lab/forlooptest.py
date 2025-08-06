#ทำด้านล่างตามจำนวนครั้งด้านบนเป็นเซต
# for x in range(10):
#     print(x)
#     for y in range(10):
#         print(y)


# for i in range(3):
#     for j in range(0,i+1):
#         if (j==1):
#             print(j, end="")


#พีระมิด
# for i in range(0,5):
#     for y in range(0,i+1):
#         print("*",end="")
#     print('\n')

# cars =["suphanut", "chalitapanukul", "41198" ]
# x = cars[1]
# print(x)

num = int(input("enter"))
numtotal = []
for i in range(num):
    data = int(input("enter your data1"))
    numtotal += [data]
print(numtotal)
numtotal.sort()#เรียงจากน้อยไปมาก
print(numtotal) 