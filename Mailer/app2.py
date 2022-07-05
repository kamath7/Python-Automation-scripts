from json import load
import yagmail
import os
from dotenv import load_dotenv
import time

load_dotenv()

pass_word = os.getenv('PASSWORD')

sender = os.getenv('SENDER_EMAIL')
receiver = os.getenv('RECEIVER_EMAIL')

subject = "Hello there 🖐"
content = '''
Just another spam email
'''

def send_email():
    yag = yagmail.SMTP(user=sender, password=pass_word)
    yag.send(to=receiver, subject=subject, contents=content)
    print("LMAO SPAMMED")

for i in range(0, 5):
    send_email()
    time.sleep(10)



