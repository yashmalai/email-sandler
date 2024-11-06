import smtplib
import os
import dotenv
import imapclient
import pyzmail
import datetime
import imaplib

imaplib._MAXLINE = 10_000_000

# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

dotenv.load_dotenv()

smtp  = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
# smtp.starttls()
smtp.login(f'{os.getenv('EMAIL')}', f'{os.getenv('PASS')}')
print(smtp.ehlo())

smtp.sendmail('islamov204@yandex.ru',
              'ilnaz204@yandex.ru',
              'Subject: test. \nTest messge to friend')
smtp.quit()

imap = imapclient.IMAPClient('imap.yandex.ru', ssl=True)
imap.login(os.getenv('EMAIL'), os.getenv('PASS'))

# imap.select_folder('INBOX', readonly=True)
# uids = imap.search(['SINCE', datetime.date(2024, 9, 20)])
# # print(uids)

# rawMessages = imap.fetch([7513], ['BODY[]', 'FLAGS'])
# mess = pyzmail.PyzMessage.factory(rawMessages[7513][b'BODY[]'])
# print(mess.get_addresses('from'))
# import pprint
# pprint.pprint(imap.list_folders())
# imap.logout()