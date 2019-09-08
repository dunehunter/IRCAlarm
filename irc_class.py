import socket
import time


class IRC:
    irc = socket.socket()

    def __init__(self):
        # Define the socket
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, channel, msg):
        # Transfer data
        self.irc.send(bytes("PRIVMSG " + channel + " " + msg + "\n", "UTF-8"))

    def connect(self, server, port):
        # Connect to the server
        print("Connecting to: " + server)
        self.irc.connect((server, port))

    def login(self, channel, botnick):
        # Perform user authentication
        self.irc.send(bytes("USER %s 0 * :%s\n" % (botnick, botnick), "UTF-8"))
        self.irc.send(bytes("NICK " + botnick + "\n", "UTF-8"))
        print(self.get_response())
        # self.irc.send(bytes("NICKSERV IDENTIFY " + botnickpass + " " + botpass + "\n", "UTF-8"))
        time.sleep(5)

        # join the channel
        self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))

    def get_response(self):
        time.sleep(1)
        # Get the response
        resps = self.irc.recv(2040).decode("UTF-8").strip().split("\n")
        for resp in resps:
            if resp.find('PING') != -1:
                self.irc.send(bytes('PONG ' + resp.split(':')[1] + '\r\n', "UTF-8"))

        return resps