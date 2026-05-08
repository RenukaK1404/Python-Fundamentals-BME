# program that calculates BMI and classifies the patient’s health category.
n=input("Enter name:")
age=int(input("Enter age:"))
h=float(input("Enter height:"))
w=float(input("Enter weight:"))
bmi = w / (h*h)
print(bmi)
if bmi<18.5:
    print("under-weight")
elif bmi>=18.5 and bmi<=24.9:
    print("Normal")
else:
    print("over-weight")