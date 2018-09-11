import unittest
from app.models import User,Comments, Pitches

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))

class CommentsUserModelTest(unittest.TestCase):

    def setUp(self):
       self.new_comment = Comments(user_id = 2, comment = 'cross buns',pitches_id = '5',date_posted='2018-09-09')

    def test_save_comment(self):

        self.assertTrue(len(Comments.query.all())>0)

class PitchesModelTest(unittest.TestCase):

    def test_save_pitch(self):
        self.assertTrue(len(Comments.query.all())>0)
