def decimal_to_binary(num):
    bin_str = "" #Initializes an empty string box. This will eventually hold and build your final binary code.
    current = num
    while current > 0:
        remainder = current % 2
        bin_str = str(remainder) + bin_str #it turns the number remainder into text data and + bin_str places the new remainder in front of whatever was already in bin_str  
        current = current // 2 # //2 divides the number by 2 and drops any decimals
    # Handles if the input is 0
    if bin_str == "":
        bin_str = "0"
    return bin_str
print(decimal_to_binary(10))
print(decimal_to_binary(25))
