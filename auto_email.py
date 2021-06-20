import smtplib
import ssl

from config import email_config

sender_email = email_config["username"]
password = email_config["password"]

receiver_email = "cshort@tcd.ie"
message = ''
with open('message.txt', 'r') as message_file:
    message = message_file.read()


port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, [receiver_email, 'cshort@tcd.ie'], message)
