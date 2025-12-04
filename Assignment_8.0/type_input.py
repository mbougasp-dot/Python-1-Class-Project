### Before starting the first thing to do is to link all my files together by importing the different functions I created in each file.
### Let's define our function first to detect the type of number entered by the user.
def detect_number_type(num_str):
    """Return 'hex' if the number from the user input starts with 0x, otherwise return 'integer'. """
    if num_str.startswith("0x") or num_str.startswith("0X"): ### This check whether the inout is a capital or small letter. It makes the input action case sensitive.
        return "hex"
    else:
        return "integer"
    ### From this function we will be able to detect the type of the entry and use it in the main program for the convertion to binary.