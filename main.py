import re
from morse_table import morse_table, DASH, DOT

# Parse text to morse assuming given text is valid
def parse_string_to_morse(str, dash='-', dot='.'):
    result = ""
    for char in str:
        if char == ' ':
            result += '[SPACE]'
        else:
            for code in morse_table[char.upper()]:
                if code == DASH:
                    result += dash
                elif code == DOT:
                    result += dot
    
    return result

if __name__ == "__main__":
    string_to_parse = input("Enter Text: ")
    regex = re.compile('^[a-zA-Z0-9 ]*$', re.I)
    
    # Check if text is valid
    if regex.match(string_to_parse):
        print(parse_string_to_morse(string_to_parse))
    else:
        print("Invalid text, Cannot be converted.")
