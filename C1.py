def ohms_current(v,r):
    current = v/r
    return current
def power_dissipated(i,r):
    power = (i*i) * r  #power = current^2/resistance
    return power
V = int(input("Enter a value of Volatge: "))
R = int(input("Enter a value of Resistance: "))
I = ohms_current(V,R) #Calls function to compute current
P = power_dissipated(I,R) 
print(f"Current = {I} A")
print(f"Power = {P} W")
