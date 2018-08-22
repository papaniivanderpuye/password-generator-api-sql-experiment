import unittest
import user_create

"""
    File Name: user_create_unit_test.py
    Written By: Papa Nii Vanderpuye
    Date: 14th August 2018
"""
"""
In this script we test the main function of user_create.py
"""


class Test(unittest.TestCase):

    def test_0_set_name(self):
        print("Start user_create test\n")

        self.assertTrue(user_create.main())
        print("SUCCESS")
        print("\nFinish user_create test\n")


if __name__ == '__main__':
    unittest.main()
