import yagmail
import os
from dotenv import load_dotenv
import pandas as pd 
load_dotenv()

df = pd.read_csv("./emails2.csv")

pass_word = os.getenv('PASSWORD')

sender = os.getenv('SENDER_EMAIL')
subject = "Hello there 🖐"

def send_email(receiver, name):
    content = [f"""\n
                Hello {name} \n
                    Spamming through Python! Bear with me 
                """, 'doge.jpg']
    yag = yagmail.SMTP(user=sender, password=pass_word)
    yag.send(to=receiver, subject=subject, contents=content)

for index, row in df.iterrows():
    try:
        send_email(row['email'], row['name'])
    except:
        raise Exception('Unable to send email!')