def detect_number_type(num_str):
    """Return 'hex' if input starts with 0x, otherwise 'integer'."""
    if num_str.startswith("0x") or num_str.startswith("0X"):
        return "hex"
    else:
        return "integer"


# "This is the parse_input module containing the detect_number_type function. To be more clear, this function recognizes the type of the input and behave according to the conditions set in the main program."