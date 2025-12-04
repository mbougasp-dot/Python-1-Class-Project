from parse_input import detect_number_type
def convert_to_binary(num_str):
    """Convert either integer or hex string to binary."""
    number_type = detect_number_type(num_str)

    if number_type == "hex":
        # Convert hex (base 16) to integer, then to binary
        number = int(num_str, 16)
    else:
        # Convert normal integer string to integer
        number = int(num_str)
        print(f"The number entered is {number} and his type is Integer") 
        
        # returns binary string like '0b1010'
    return bin(number) # Strip the '0b' prefix
# Hint: Be careful with the indentation of the return statement !!!!
# That is why my code was not working before.