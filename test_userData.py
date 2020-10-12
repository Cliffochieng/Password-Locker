import unittest
from userData import UserData

class TestuserData(unittest.TestCase):
    def setUp(self):
        """
        set up method
        """
        self.new_user = UserData("cliff", "ochieng", "cliffochieng844@gmail.com", "cliffochieng", "yoloyolo") 

    def test_init(self):
        """
        testing initialization of class
        """
        self.assertEqual(self.new_user.firstName, "cliff")
        self.assertEqual(self.new_user.lastName, "kasera")
        self.assertEqual(self.new_user.email, "ckasera@gmail.com")
        self.assertEqual(self.new_user.username, "Blankphrase")
        self.assertEqual(self.new_user.password, "lololo")