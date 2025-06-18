bill_amount, tip_percent, num_people = map(float, input("Enter bill amount, tip %, and number of people: ").split())

tip_amount = bill_amount * (tip_percent / 100)

total_bill = bill_amount + tip_amount

amount_per_person = total_bill / num_people

print(f"Each person pays: {amount_per_person:.2f}")

# คำถาม: อาชีพใดที่จำเป็นต้องใช้?
# ตอบ: อาชีพที่เกี่ยวกับร้านอาหารเช่น พนักงานร้านอาหาร,
#  ผู้จัดการร้าน, หรือเจ้าของธุรกิจร้านอาหารที่ต้องใช้สรุปค่าใช้จ่าย