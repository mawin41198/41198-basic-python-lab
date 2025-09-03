line = input().strip()

mid = len(line) // 2
a = line[:mid]
b = line[mid:]

if a.lower() < b.lower():
    print("A comes before B")
elif a.lower() > b.lower():
    print("A comes after B")
else:
    print("A equals B")
