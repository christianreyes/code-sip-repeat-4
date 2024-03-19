import unittest
import csr_password_gen

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class Testing(unittest.TestCase):
   def test_random_lower(self):
       rl = csr_password_gen.random_lower()  # generate random lower letter
       self.assertIn(rl, lower_letters)      # if letter is in the list, return true

if __name__ == '__main__':
   unittest.main()                           # run the unit tests if file ran as script
   