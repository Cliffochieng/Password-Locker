import unittest
from userData import UserData

class TestuserData(unittest.TestCase):
    def setUp(self):
        """
        set up method
        """
        self.new_user = UserData("cliff", "ochieng", "cliffochieng844@gmail.com", "cliffochieng", "yoloyolo") 