first_side = float(input("Enter first side: "))
second_side = float(input("Enter second side: "))
third_side = float(input("Enter third side: "))

if first_side + second_side > third_side or second_side + third_side > first_side or first_side + third_side > second_side:
  print ("The figure is a triangle")
else: 
  print ("The figure is NOT a triangle")