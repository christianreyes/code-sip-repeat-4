import random

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def random_lower():
    return random.choice(lower_letters)

def generate_complex_password(complexity_string: str):
    """
    Function which generates a complex password given a complexity input string

    Inputs:

    complexity_string: str
        Concatination of characters which define the complexity: 
        - "L" for a random lowercase letter

    Output:
    A random complex password conforming with the input complexity string requirements
    """
    password_chars = [] # list for storing the generated password characters

    for c in complexity_string: # loop through each character of the complexity string
        if c == "L": # if the current character matches "L"
            password_chars.append(random_lower()) # add the random lower letter to the end of the list
    
    random.shuffle(password_chars) # randomly shuffle all the characters in the list
    return "".join(password_chars) # combine all the characters in the list into a single string and return it

def main():
    print("Hello, World! This is the Code.Sip.Repeat Random Password generator")
    print(f"Your random password is { generate_complex_password("LLLLL") }") # replace with our new function and an input complexity string. "LLLLL" as the example should generate 5 random lowercase letters, shuffled

if __name__ == "__main__":
    main()
    