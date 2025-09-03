line = input()

atpos = line.find('@')

spacepos = line.find(' ', atpos)

domain = line[atpos+1 : spacepos]
print(domain)
#หาตัวที่อยู่ระหว่าง@กับspacebar
