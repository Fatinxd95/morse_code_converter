from morse_map import morse_code

# Main function
def main():
    # Takes input from the user and converts it to uppercase letters and stores the return value into text
    text = input("Enter the text: ").upper()
    # Calls the convert function with the argument text
    convert(text)

# Conversion function
def convert(text):
    # For each characters in text 
    for characters in text:
        print(morse_code[characters], end=" ")

# Calls the main function
main()
