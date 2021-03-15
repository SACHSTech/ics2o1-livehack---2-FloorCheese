antennas_input = int(input("Enter amount of antenna: "))
eyes_input = int(input("Enter amount of eyes: "))

if antennas_input >= 3 and eyes_input <= 4:
  print ("Life form detected: AudreyMartian")
  
  if antennas_input <= 6 and eyes_input >= 2:
      print ("Life form detected: MaxMartian")
  
  elif antennas_input <= 2 and eyes_input >= 3:
    print ("Life form detected: BrooklynMartian")
  
  elif antennas_input == 0 and eyes_input == 2:
    print ("Life form detected: MattDamonMartian")
  
  else:
    print ("No life form detected")