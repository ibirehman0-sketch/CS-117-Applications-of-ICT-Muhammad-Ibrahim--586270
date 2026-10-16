def star_to_delta( Ra, Rb, Rc):
    J = (Ra *Rb) + (Rb * Rc) + (Rc * Ra) #calculates common numerator sum factor (K) for star to delta
    Rab = J / Rc #computes first delta resistor value
    Rbc = J / Ra
    Rca = J / Rb
    return round(Rab, 2), round(Rbc, 2), round(Rca, 2) #round is a function which rounds up the decimal upto a point
print(star_to_delta(10, 20, 30))
