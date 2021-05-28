import smtplib

s = smtplib.SMTP("smtp.gmail.com", 587)
sender_email_id = "3981212@myuwc.ac.za"
receiver_email_id = "thabosetsubi3@gmail.com"
password = input("Enter your email password: ")

s.starttls()

s.login(sender_email_id, password)

message = "hi how are you\n"

s.sendmail(sender_email_id, receiver_email_id, message)

s.quit()
