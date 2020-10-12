import unittest
from userData import UserData

class TestuserData(unittest.TestCase):
    def setUp(self):
        """
        set up method
        """
        self.new_user = UserData("clifford", "ochieng", "cliffordochieng844@gmail.com", "cliffochieng", "yoloyolo") 

    def test_init(self):
        """
        testing initialization of class
        """
        self.assertEqual(self.new_user.firstName, "clifford")
        self.assertEqual(self.new_user.lastName, "ochieng")
        self.assertEqual(self.new_user.email, "cliffordochieng844@gmail.com")
        self.assertEqual(self.new_user.username, "cliffochieng")
        self.assertEqual(self.new_user.password, "yoloyolo")

    def tearDown(self):
        """
        restart
        """
        UserData.create_account = []

    def test_save_account(self):
        """
        testing save account method
        """
        self.new_user.save_account() 
        self.assertEqual(len(UserData.create_account), 1)
 


if __name__ == '__main__':
    unittest.main()
        