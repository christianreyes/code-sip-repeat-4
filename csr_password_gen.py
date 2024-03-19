import random
import string      # so we can use the pre-defined ascii character lists

lower_letters = string.ascii_lowercase # check the documentation, pre-defined
upper_letters = string.ascii_uppercase
numbers = string.digits

def random_lower():
    return random.choice(lower_letters)

def random_upper():
    return random.choice(upper_letters)

def random_number():
    return random.choice(numbers)

def generate_complex_password(complexity_string: str):
    """
    Function which generates a complex password given a complexity input string

    Inputs:

    complexity_string: str
        Concatination of characters which define the complexity:
        - "L" for a random lowercase letter
        - "U" for a random uppercase letter
        - "N" for a random number
        - "W" for a wildcard (any character from the above)

    Output:
    A random complex password conforming with the input complexity string requirements
    """
    password_chars = [] # list for storing the generated password characters

    for c in complexity_string: # loop through each character of the complexity string
        if c == "L": # if the current character matches "L"
            password_chars.append(random_lower()) # add the random lower letter to the end of the list
        elif c == "U": # if the current character matches "U"
            password_chars.append(random_upper()) # add the random upper letter to the end of the list
        elif c == "N": # if the current character matches "N"
            password_chars.append(random_number())
        elif c == "W": # if wildcard
            rand_function = random.choice([random_lower, random_upper, random_number]) # lists can contain any values, even functions!
            password_chars.append(rand_function()) # call the function which was selected above

    
    random.shuffle(password_chars) # randomly shuffle all the characters in the list
    return "".join(password_chars) # combine all the characters in the list into a single string and return it

def main():
    print("Hello, World! This is the Code.Sip.Repeat Random Password Generator")
    print(f"Your random password is: { generate_complex_password('LLLUUUNNNWWW') }") # replace with our new function and an input complexity string. "LLLUUU" as the example should generate 3 random lowercase, uppercase, numbers, and 3 wildcard,  shuffled

if __name__ == "__main__":
    main()
