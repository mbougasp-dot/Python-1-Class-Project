
# ----------------- MAIN PROGRAM -----------------
from parse_input import detect_number_type
from binary_convert import convert_to_binary
# Get user input
user_input = input("Enter a number (Either integer or a hex starting with 0x for instance 14 is an integer but to represent a hex, inter 0xValue_of_hexadecimal_number): ")

# 1. Detect type of the number:
num_type = detect_number_type(user_input)
print(f"You entered a(n) {num_type} number.")
 
# 2. Convert to binary
binary_value = convert_to_binary(user_input)
print(f"Binary representation: {binary_value}")





##For this try the code doesn't work when I try to enter a hex number like 0x1A i don't know why!!