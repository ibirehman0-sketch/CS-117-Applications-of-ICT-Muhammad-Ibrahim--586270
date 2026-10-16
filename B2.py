n = int(input("How mnay resistiors? "))
Rtotal = 0 # Initializes total resistance to be 0
for x in range(1, n + 1):
    cont = int(input(f" Enter R{x}")) #Promts the user to enter the value for each indiviual resistor
    Rtotal = cont + Rtotal
print("The total resistance =", Rtotal, "ohm")
