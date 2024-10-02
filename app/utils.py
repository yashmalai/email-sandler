from imapclient import IMAPClient
import os
import dotenv
import pyzmail
import imaplib

imaplib._MAXLINE = 10_000_000

dotenv.load_dotenv()


def get_emails(folder='INBOX'):
    with IMAPClient(os.getenv("IMAP_SERVER"), ssl=True) as client:
        client.login(os.getenv("EMAIL"), os.getenv("PASS"))
        client.select_folder(folder, readonly=True)
        messages = client.search('ALL')
        emails = []
        for msg_id in messages[-20:]:
            raw_message = client.fetch([msg_id], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(raw_message[msg_id][b'BODY[]'])
            subject = message.get_subject()
            from_email = message.get_address('from')
            emails.append({'subject': subject, 'from': from_email})
        return emails