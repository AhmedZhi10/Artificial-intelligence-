def bodymassindex(height, weight):
    return round((weight / height**2),2)


h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))


print("Welcome to the BMI calculator.")

bmi = bodymassindex(h, w)
print("Your BMI is: ", bmi)

