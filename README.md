# Code.Secure.Protect

[Code.Sip.Repeat 4.0](https://codesiprepeat.com/) instructional material, by Christian Reyes.

## Random Password Generator

The `csr_password_gen.py` python file generates a "random" secure password based on the following password complexity input string:

- "L" for a random lowercase letter
- "U" for a random uppercase letter
- "N" for a random number
- "W" for a wildcard (any character from the above)

Example: generate_complex_password(“LLUNW”) = random password with at least 2 lower case letters, one uppercase letter, one number, and a wildcard which can be a lower, upper, or number.

## Password Generator Website

The `csr_web_server.py` python file creates a http web server which serves a html page and form for submitting a password complexity requirement input and receiving a password back.