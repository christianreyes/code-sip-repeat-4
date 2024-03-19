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

   # if there is an item in the list, remove one and return true, otherwise false
   def _check_list(self, l):
      if len(l) > 0:
         l.pop()
         return True
      else:
         return False

   def check_complex_password(self, password=None, complexity_str=None):
      results = True

      r_lowers = []
      r_uppers = []
      r_numbers = []
      r_unknowns = []

      # categorize every character in the password
      for c in password:
         if c in lower_letters:
            r_lowers.append(c)
         elif c in upper_letters:
            r_uppers.append(c)
         elif c in numbers:
            r_numbers.append(c)
         else:
            r_unknowns.append(c)

      rest_of_characters = None

      results = True

      # for each letter in complexity string, check against categorized characters
      # boolean logic, true and= false = false, true and=true = true, &= is and=
      for c in complexity_str:
         if c == "L":
            results &= self._check_list(r_lowers)
         elif c == "U":
            results &= self._check_list(r_uppers)
         elif c == "N":
            results &= self._check_list(r_numbers)
         elif c == "W":
            if rest_of_characters is None:
                  rest_of_characters = r_lowers + r_uppers + r_numbers
            
            results &= self._check_list(rest_of_characters)

      return results
   
   def test_manual_passwords(self):
      # Expect these to pass
      # ===================

      # Check lowercase
      self.assertTrue(self.check_complex_password(password="abc", complexity_str="LLL"))

      # Check Uppercase
      self.assertTrue(self.check_complex_password(password="TYXCT", complexity_str="UUUU"))

      # Check Numbers
      self.assertTrue(self.check_complex_password(password="98712", complexity_str="NNNNN"))

      # Check mixed
      self.assertTrue(self.check_complex_password(password="123abc", complexity_str="LLLNNN"))

      # Check mixed + any
      self.assertTrue(self.check_complex_password(password="12Nh6zxAS", complexity_str="LLUUNNWWW"))

      # Expect these to fail
      # ===================
      self.assertFalse(self.check_complex_password(password="123!@#", complexity_str="LLLNNN"))

   def test_100_passwords(self):
      for i in range(100):
         complexity_str = "LLLUUUNNNWWW"
         password = csr_password_gen.generate_complex_password(complexity_string=complexity_str)
         self.assertTrue(self.check_complex_password(password=password, complexity_str=complexity_str))

if __name__ == '__main__':
   unittest.main()                           # run the unit tests if file ran as script
