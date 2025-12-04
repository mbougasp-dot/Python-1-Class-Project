### Before starting the first thing to do is to link all my files together by importing the different functions I created in each file.
### Let's import the function from my type_input file to use it here.
from type_input import detect_number_type

### Now let's define our function to convert the number entered by the user to binary.
def convert_to_binary(num_str):
    """convert either integer or hex string to binary Instruction code !!."""
    number_type = detect_number_type(num_str)
    
    if number_type == "