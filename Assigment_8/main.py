
# ----------------- MAIN PROGRAM -----------------
from parse_input import detect_number_type
from binary_convert import convert_to_binary
# Get user input
user_input = input("Enter a number (integer or hex starting with 0x): ")

# 1. Detect type
num_type = detect_number_type(user_input)
print(f"You entered a {num_type} number.")

# 2. Convert to binary
binary_value = convert_to_binary(user_input)
print(f"Binary representation: {binary_value}")
