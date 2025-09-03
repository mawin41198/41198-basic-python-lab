x = ' win'
# print(x[0:4])#print suph
# print(x[6:7])#print u
# print(x[6:25])#print ut chalitapanukul
# print(x[:2])#printตัวที่อยู่ข้างหลัง


# if x == 'banana':
#     print("All right")
# if x < 'banana':
#     print('your word,' + x +'come before banana')
# elif x > 'banana':
#     print('your word,' + x + 'come after banana')
# else:
#     print("All right banana")


# greet = 'hello bob'
# m = greet.replace('bob', 'jane')
# print(m)




# if ('m' in x):
#     print("true")
# else:
#     print("false")

data = 'From stephen.marquard@uct.ac.za Sat jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos) 
print(sppos)
host = data[atpos+1 : sppos]
print(host)