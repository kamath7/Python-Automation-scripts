from json import load
import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

pass_word = os.getenv('PASSWORD')

sender = os.getenv('SENDER_EMAIL')
receiver = os.getenv('RECEIVER_EMAIL')

subject = "Hello there 🖐"
content = ["""
Spamming through Python! Bear with me 
""", 'doge.jpg']

yag = yagmail.SMTP(user=sender, password=pass_word)
yag.send(to=receiver, subject=subject, contents=content)