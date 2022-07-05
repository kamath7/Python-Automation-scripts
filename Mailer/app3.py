from dotenv import load_dotenv
import os 
import pandas as pd
import yagmail

load_dotenv()

sender = os.getenv("SENDER_EMAI")
pass_word = os.getenv("PASSWORD")

subject = "Hello there 🖐"
df = pd.read_csv("email.csv")
content = '''
Just another spam email
'''

def send_email(receiver):
    yag = yagmail.SMTP(user=sender, password=pass_word)
    yag.send(to=receiver, subject=subject, contents=content)
    print("LMAO SPAMMED")

