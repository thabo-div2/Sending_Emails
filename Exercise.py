# Exercise
# Sending emails to multiple recipients

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
s = smtplib.SMTP("smtp.gmail.com", 587)
sender = "3981212@myuwc.ac.za"
recipients = ["godwin@lifechoices.co.za, thabosetsubi3@gmail.com, mujaid.kariem@gmail22.com"]
password = input("Enter password: ")

s.starttls()

s.login(sender, password)

message = MIMEMultipart()
message["Subject"] = "Greetings"
message["From"] = sender
message["To"] = ",".join(recipients)
s.sendmail(sender, recipients, message.as_string())

s.quit()
