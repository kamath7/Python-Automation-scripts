from json import load
import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

pass_word = os.getenv('PASSWORD')

sender = os.getenv('SENDER_EMAIL')
receiver = os.getenv('RECEIVER_EMAIL')

subject = "Hello there 🖐"
content = '''
Welcome to the awesome party at my place!
'''

yag = yagmail.SMTP(user=sender, password=pass_word)
yag.send(to=receiver, subject=subject, contents=content)