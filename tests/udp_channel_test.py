import unittest

# append parent directory to import path
import env

# now we can import the lib module
from udp_channel import UDPChannel

class UDPChannelTest(unittest.TestCase):

	def test_rio_to_sonar(self):
		rio = UDPChannel()
		sonar = UDPChannel(local_port=UDPChannel.default_remote_port,
						   remote_port=UDPChannel.default_local_port)
		message = "Start"
		rio.send_to(message)
		(recv_message, sender_info) = sonar.receive_from()
		# make sure we got the message
		self.assertEqual(recv_message, message)
		# check for the address of the sender
		self.assertEqual(sender_info[0], UDPChannel.default_local_address)
		# cleanup for next test
		sonar.close()
		rio.close()
	
	def test_sonar_to_rio(self):
		rio = UDPChannel()
		sonar = UDPChannel(local_port=UDPChannel.default_remote_port,
						   remote_port=UDPChannel.default_local_port)
		message = "Range"
		sonar.send_to(message)
		(recv_message, sender_info) = rio.receive_from()
		# check that the message was received
		self.assertEqual(recv_message, message)
		# check for the proper sender address
		self.assertEqual(sender_info[0], UDPChannel.default_local_address)
		# clean up
		sonar.close()
		rio.close()

if __name__ == '__main__':
    unittest.main()

