day = int(input())
if 1 <= day <= 7:
    if (day == 6 or day == 7):
        print("Weekend")
    else:
        print("weekday")
else:
    print("กรอก1-7เท่านั้น")