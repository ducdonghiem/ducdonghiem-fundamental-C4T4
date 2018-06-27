m=float(input("Height in cm ?"))/100
kg=float(input("Weght in kg ?"))
bmi=kg/(m*m)
print("Your BMI is ", bmi)
if bmi<16:
    print("You are severely underweght !")
if 16<=bmi<18.5:
    print("You are underweght")
if 18.5<=bmi<25:
    print("You are normal")
if 25<bmi<=30:
    print("You are overweight")
if bmi>30:
    print("You are obese !")                 
