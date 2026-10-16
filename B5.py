R1 = 0
R5 = 0
R_rejected = 0
x = float(input("Enter resistance (0 to stop): ")) #input to start the loop
while x != 0:
    if 99.0 <= x <= 101.0:
        R1 += 1
    elif 95.0 <= x <= 105.0:
        R5 += 1
    else:
        R_rejected += 1
    x=float(input("Enter resistance (0 to stop): ")) #prompts for the next resistance
print ("1% Tolerance:", R1)
print ("5% Tolerance:", R5)
print ("Rejected:", R_rejected)
