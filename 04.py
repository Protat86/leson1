feet = int(input("Feet: "))
inches = int(input("Inches: "))

total_inches = feet * 12 + inches
height_cm = total_inches * 2.54

print("Height in centimeters:", height_cm)
