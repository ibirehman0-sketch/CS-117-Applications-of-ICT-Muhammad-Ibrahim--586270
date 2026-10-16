def parallel_resistance(resistors):
    sum_reciprocal = 0
    rle = len(resistors) #counts total number of resistors
    for x in range(rle):
        sum_reciprocal += 1 / resistors[x] #adds reciprocal of each resistor to the sum
    Req = 1 / sum_reciprocal #flips reciprocal sum back over to find R_eq
    return Req
# Test cases matching the sample run
R1 = [10, 10]
R2 = [100, 200, 300]
c = parallel_resistance(R1)
v = parallel_resistance(R2)
print("Parallel Resistance 1:", c)
print("Parallel Resistance 2:", v)
