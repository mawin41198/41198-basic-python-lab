คะแนนเก็บ = int(input("enter your point1"))
(0<คะแนนเก็บ>=30)
คะแนนสอบกลางภาค = int(input("enter your point2"))
(0<คะแนนสอบกลางภาค>=30)
คะแนนสอบปลายภาค = int(input("enter your point3"))
(0<คะแนนสอบปลายภาค>=40)
grade =(คะแนนเก็บ + คะแนนสอบกลางภาค + คะแนนสอบปลายภาค)
if (grade>=80):
    print("A")
elif (grade>=75):
    print("B+")
elif (grade>=70):
    print("B")
elif (grade>=65):
    print("C+")
elif (grade>=60):
    print("C")
elif (grade>=55):
    print("D+")
elif (grade>=50):
    print("D")
elif (grade<50):
    print("F")