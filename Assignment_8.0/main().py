### Before starting the first thing to do is to link all my files together by importing the different functions I created in each file.
### To start here in the main i will inmport my differents functions from the other files.
from binary_conv import convert_to_binary
from type_input import detect_number_type
### Now let's create the main function to execute the program.
user_input = input("Enter a Integer of Hexadecimal number (using a prefix 0x or 0X for the hexadecimal value)")
"""Main function to execute the binary conversion program, handling the user's input. """

#1. Detect the type of number entered by the user.
num_type = detect_number_type(user_input)
print(f"You entered a(n) {num_type} number.")
    
if num_type == "hex":
        print(f"The hexadecimal number you have entered is : {user_input}")
        
    #2. Convert to binary
binary_value = convert_to_binary(user_input)
print(f"The number in binary representation is : {binary_value} ")
    
    #At this stage let's check if everything is working fine by running the main function.
    #First Error detected while running the program.
    
    