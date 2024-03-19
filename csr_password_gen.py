import random

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def random_lower():
    return random.choice(lower_letters)

def main():
    print("Hello, World! This is the Code.Sip.Repeat Random Password generator")
    print(f"Your random password is { random_lower() }") # this called a f-string and will run the code in between the {} which will substitute the output of our function

if __name__ == "__main__":
    main()
