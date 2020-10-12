import unittest

from credentialsData import CredentialsData

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        setUp method
        """
        self.new_credential = CredentialsData("Gmail", "cliff", "lolololo") 