import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import hash_utilities

class TestHashUtilities(unittest.TestCase):
    def test_password_hash_chek(self):
        test_pwd = 'test-password'
        expected_hash = '$2b$12$J/vA6E382SLd2hbrCX/3Gee.nNOlY7hozijsrpUPY/ihL1PTBic/C'
        
        self.assertEqual(hash_utilities.password_hash_check(password=test_pwd,hash=expected_hash),True)


if __name__ == '__main__':

    unittest.main()    