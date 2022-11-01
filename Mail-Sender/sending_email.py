from email.mime.multipart import MIMEMultipart

# to send text
from email.mime.text import MIMEText

# to send image s
from email.mime.image import MIMEImage

# to send audio
from email.mime.audio import MIMEAudio

import smtplib

message = MIMEMultipart()

message["from"] = "Aashish Sharma"
message["to"] = "email"
message["subject"] = "just a random subject"

# attachment can be text, image, document and so on
message.attach(MIMEText("How are you, buddy?"))

# it's smtp protocol provider
smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)

# it's like saying hello to smtp protocol
smtp.ehlo()

# it's encrypt the data we sent
smtp.starttls()

# loging in
smtp.login("email", "password")

# sending message
smtp.send_message(message)

# closing smptp protocol or object
smtp.close()

print("Sent")
