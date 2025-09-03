line = input().strip()

num_str = ''
animal = ''
for c in line:
    if c.isdigit() or c == '.':
        num_str += c
    else:
        animal += c

number = float(num_str)

years = int(number // 10)
animals = round(number % 10, 6) 

print(f"In {years} years I have spotted {animals} {animal}.")
