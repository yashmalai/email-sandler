import smtplib
import os
import dotenv
import imapclient
import pyzmail

# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

dotenv.load_dotenv()

# smtp  = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
# # smtp.starttls()
# smtp.login(f'{os.getenv('EMAIL')}', f'{os.getenv('PASS')}')
# print(smtp.ehlo())

imap = imapclient.IMAPClient('imap.yandex.ru', ssl=True)
imap.login(os.getenv('EMAIL'), os.getenv('PASS'))

imap.logout()