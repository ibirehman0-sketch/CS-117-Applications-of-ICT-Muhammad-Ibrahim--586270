readings = (3.3,3.1,3.4,2.9,3.6,3.0,3.2)
max,Vabove = 0,0 #initializes maximum tracking variable and a counter for values above 3.2V
min, sum = 100000000, 0
for x in range(7):
    if readings[x] > max: 
        max = readings[x]
    if readings[x] < min:
        min = readings[x]
    sum = sum + readings[x] #adds current reading to the running sum
    if readings[x] > 3.2:
        Vabove = Vabove + 1
print("Readings above 3.2 V: ",Vabove)
print("Highest: ",max,"V")
print("Lowest: ",min,"V")
print("Average: ",sum/7,"V") #Calculates and outputs the average voltage across the 7 readings
