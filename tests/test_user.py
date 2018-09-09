import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
<<<<<<< HEAD
        self.assertTrue(self.new_user.pass_secure is not None)
=======
        self.assertTrue(self.new_user.password_hash is not None)
>>>>>>> dev

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

<<<<<<< HEAD
        def test_password_verification(self):
=======
    def test_password_verification(self):
>>>>>>> dev
            self.assertTrue(self.new_user.verify_password('banana'))
