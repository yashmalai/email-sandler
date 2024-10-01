import smtplib
import os
import dotenv
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

dotenv.load_dotenv()

smtp  = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
# smtp.starttls()
print("Введите логин")
smtp.login(f'{os.getenv('EMAIL')}', f'{os.getenv('PASS')}')
smtp.ehlo()

