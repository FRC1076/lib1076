import unittest

# append parent directory to import path
import env

# now we can import the lib module
from udp_channel import UDPChannel

class UDPChannelTest(unittest.TestCase):
	def send_to_receive_from_test(self):
		"""
		Save this channel in instance variable so
		we can test it in subsequent tests.
		"""
		self.rio = UDPChannel()
		self.sonar = receiver = UDPChannel(local_port=UDPChannel.default_remote_port,
							           	   remote_port=UDPChannel.default_local_port)
		message = "Start"
		self.rio.send_to(message)
		(recv_message, sender_info) = self.sonar.receive_from()
		self.assertEqual(recv_message, message)
	

if __name__ == '__main__':
    unittest.main()

