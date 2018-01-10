import unittest
from  app.common.models import User

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
	u = User(password = 'cat')
	self.assertTrue(u.password.hash is not None)

    def test_no_password_getter(self):
	u = User(password = 'cat')
	with self.assertRaises(AttributeError):
	    u.password

    def test_passwrod_salts_are_random(self):
	u = User(password='cat')
	u2 = User(password='cat')
	self.assertTrue(u.password_hash != u2.password_hash)


