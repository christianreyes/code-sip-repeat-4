import unittest           # required to access the test infrastructure functions
import csr_password_gen   # import the code we previously wrote (random.py must be in the same folder!)

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

class Testing(unittest.TestCase):
   def test_random_lower(self):
      rl = csr_password_gen.random_lower()  # generate random lower letter
      self.assertIn(rl, lower_letters)      # if letter is in the list, return true

   def test_random_upper(self):
      ru = csr_password_gen.random_upper()  # generate random lower letter
      self.assertIn(ru, upper_letters)      # if letter is in the list, return true

   def test_random_number(self):
      rd = csr_password_gen.random_number()  # generate random digit
      self.assertIn(rd, numbers)      # if letter is in the list, return true

if __name__ == '__main__':
   unittest.main()                           # run the unit tests if file ran as script
