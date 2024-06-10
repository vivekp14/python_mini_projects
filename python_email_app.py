from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'vipin.prakash474@gmail.com'
email_password = password

email_receiver = 'diceco5216@jadsys.com'

subject = "Important Message"
body = """
The Message is very clear, keep yourself healthy
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject 
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
