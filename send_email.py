from email.headerregistry import Address
from email.message import EmailMessage
import smtplib
# Gmail details
from utilities import GMAIL_ADDRESS, GMAIL_APPLICATION_PASSWORD


# Recipent
to_address = (
    Address(display_name='Yu Fang', username='yu.fang2013', domain='icloud.com'),
)

def create_email_message(from_address, to_address, subject, body):
    msg = EmailMessage()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_content(body)
    return msg


def send_email_to_user():
    msg = create_email_message(
        from_address=GMAIL_ADDRESS,
        to_address=to_address,
        subject='Hello World',
        body="Test sending the body.",
    )

    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(GMAIL_ADDRESS, GMAIL_APPLICATION_PASSWORD)
        smtp_server.send_message(msg)

    print('Email sent successfully')