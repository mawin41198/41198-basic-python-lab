eggs_input = input()

# แปลงเป็นจำนวนเต็ม
eggs = int(eggs_input)

# คำนวณจำนวนแผงและไข่ที่เหลือ
panels = eggs // 30  # จำนวนแผงที่จัดได้
remainder = eggs % 30  # จำนวนไข่ที่เหลือ

# แสดงผลลัพธ์
print(f"สามารถจัดได้ {panels} แผง และเหลือ {remainder} ฟอง")