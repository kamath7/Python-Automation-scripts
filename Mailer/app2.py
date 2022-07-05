from json import load
import yagmail
import os
from dotenv import load_dotenv
import time
from datetime import datetime as dt 


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

while True: 

    if dt.now().hour == 23 and dt.now().minute == 9:
        send_email()
        break


