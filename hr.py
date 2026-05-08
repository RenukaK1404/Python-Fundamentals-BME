pn=input("Enter name:")
hr=int(input("Enter heart rate:"))
if hr<60:
    print("Bradycardia")
elif hr>=60 and hr<=100:
    print("Normal")
elif hr>100 and hr<=140:
    print("elevatedHR")
else: 
    print("Dangerous")