height = float(input("Enter your height(cm): "))
weight = float(input("Enter your weight(kg):"))
height_m = height / 100
bmi =  weight / (height_m ** 2)
if bmi < 18.5:
    print("You're underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You're overweight.")
else:
    print("You're in the obese range.")
