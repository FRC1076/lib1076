import socket
#
#  Create the infra for two-way communication channel using UDP
#  Set receive from timeout to .001 seconds to avoid blocking for
#  long.
#
class UDPChannel:
        """
        Create a communication channel to send and receive messages
        between two addresses and ports.
        Defaults are loopback address with specific port address.
        timeout_in_seconds is the receive_from time out value.
        """
        default_local_port = 5888
        default_remote_port = 5880
        # Useful defaults permit minimal arguments for simple test.
        # On one end:
        #      sender = UDPChannel()
        # On the other end (in another window/program)
        #    receiver = UDPChannel(local_port=sender.remote_port, remote_port=sender.local_port)
        def __init__(self,
                     local_ip="127.0.0.1",
                     local_port=default_local_port,
                     remote_ip="127.0.0.1",
                     remote_port=default_remote_port,
                     timeout_in_seconds=0.001, receive_buffer_size=8192):
                """Create the sending and receiving sockets for a communcation channel"""
                try:
                        self.local_ip = local_ip
                        self.local_port = local_port
                        self.remote_ip = remote_ip
                        self.remote_port = remote_port

                        # create the receive socket
                        self.receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        self.receive_socket.bind((local_ip, local_port))

                        # and the sending socket
                        self.send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                        # cache other configurable parameters
                        self.timeout_in_seconds = timeout_in_seconds
                        self.receive_buffer_size = receive_buffer_size
                except:
                        print("Something went wrong")

        def send_to(self, message):
                """send message to the other end of the channel"""
                self.send_socket.sendto(message.encode(), (self.remote_ip, self.remote_port))
        def reply_to(self, message, ip, port):
                """reply to a message from the other end of the channel."""
                self.send_socket.sendto(message.encode(), (ip, port))

        def receive_reply(self):
                """receive a reply"""
                self.send_socket.settimeout(self.timeout_in_seconds)
                return self.send_socket.recvfrom(self.receive_buffer_size)

        def receive_from(self):
                """
                wait for timeout to receive a message from channel
                If there is a timeout, return None,None
                Otherwise return (decoded_message, addr_n_port)
                """
                self.receive_socket.settimeout(self.timeout_in_seconds)
                try:
                        (message, portaddr) = self.receive_socket.recvfrom(self.receive_buffer_size)
                except socket.timeout as e:
                        (message, portaddr) = (None, None)
                if message is not None
                        message = message.decode()
                return (message, portaddr)

