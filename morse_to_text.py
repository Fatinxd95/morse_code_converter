from morse_code import reversed_morse_code

# Main function
def main():
    # Takes input from the user and converts it to a list and stores the return value into morse_code variable
    morse_code = input("Enter the text: ").split(" ")
    # Calls the convert function with the argument morse_code
    convert(morse_code)

# Conversion function
def convert(morse_code):
    # For each characters in text
    for characters in morse_code:
        print(reversed_morse_code[characters], end="")

# Calls the main function
main()
