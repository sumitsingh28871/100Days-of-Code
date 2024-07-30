#greeting to the user
print ("Welcome to the BMI Calculator")

#Ask the user about their height 
height = float(input("What's your height?\n"))
#Converting height from meters to centimeters 
if height > 10:
    height_in_meters = height/100
else:
    height_in_meters = height

#Ask the user about their weight
weight = float(input("What's your body weight?\n"))

#Calculating BMI
BMI = weight/height_in_meters ** 2
print ("Your BMI is" + " " + str(int(BMI)))

if BMI < 18.5:
    print ("You are in the UNDERWEIGHT range")
elif 18.5 <= BMI <= 24.9:
    print ("You are in the HEALTHY range")
elif 25 <= BMI <= 29.9:
    print ("You are in the OVERWEIGHT range")
else:
    print ("You are in the OBESE range")