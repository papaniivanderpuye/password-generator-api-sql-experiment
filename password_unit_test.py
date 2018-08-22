
import unittest
from account_generator import *

"""
    File Name: password_unit_test.py
    Written By: Papa Nii Vanderpuye
    Date: 14th August 2018
"""
"""
In this script we test various inputs on the generate_password
and check_password_level functions
"""


class Test(unittest.TestCase):

    def test_0_set_name(self):
        print("Start generate_password and check_password_level test\n")

        for complexity in range(-2, 50):
            for length in range(-2, 50):
                if(complexity < 1 or complexity > 4 or length < complexity):
                    self.assertIsNone(generate_password(length, complexity))
                else:
                    password = generate_password(length, complexity)
                    predicted_level = check_password_level(password)
                    if(complexity < 3 and length > 7):
                        self.assertEqual(complexity + 1, predicted_level)
                    else:
                        print(password, "check level", predicted_level)
                        self.assertEqual(complexity, predicted_level)
        print("\nSUCCESS\n")
        print("\nFinish generate_password and check_password_level test\n")


if __name__ == '__main__':
    unittest.main()
