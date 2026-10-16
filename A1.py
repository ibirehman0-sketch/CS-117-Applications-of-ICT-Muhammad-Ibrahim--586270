Voltage = int(input("Enter the value of (V): "))
Resistance = int(input("Enter the value of (R): "))
if Resistance <= 0:
        print("Invalid resistance") #prevents errors
else:
    current = Voltage/ Resistance
    print("Current =",current)
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
    
