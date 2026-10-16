def loaded_divider( V_source, R1, R2, R_load):
    V_unloaded = V_source * R2 / (R1 + R2) #calculates standard ideal output voltage without a load
    R_eq = (R2 * R_load) / (R2 + R_load)
    V_loaded = V_source * R_eq / (R1 + R_eq) #calculates true output volatge uner load using R_eq
    return V_unloaded, V_loaded
print(loaded_divider(12, 100, 1000, 500))
