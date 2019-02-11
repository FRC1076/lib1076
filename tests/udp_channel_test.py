import unittest

# append parent directory to import path
import env

# now we can import the lib module
from UDPChannel import UDPChannel

class UDPChannelTest(unittest.TestCase):
    def test_DefaultChannel(self):
	"""
	Save this channel in instance variable so
	we can test it in subsequent tests.
	"""
	self.chan = UDPChannel()
	

if __name__ == '__main__':
    unittest.main()

