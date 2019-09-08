from irc_class import *
from send_email import send_email_to_user
from utilities import server, port, channel, botnick

MAXIUM_SENT_COUNT = 20

irc = IRC()
irc.connect(server, port)
irc.login(channel, botnick)

while True:
    texts = irc.get_response()
    for text in texts:
        print(text)

        trigger_msg = "@@@@@@__LAMP_EVENT__@@@@@@"
        if "PRIVMSG" in text and botnick in text and trigger_msg in text:
            for _ in range(MAXIUM_SENT_COUNT):
                send_email_to_user()
                time.sleep(5)
