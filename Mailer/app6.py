import yagmail
import os
from dotenv import load_dotenv
import pandas as pd 
load_dotenv()

df = pd.read_csv("./emails3.csv")

pass_word = os.getenv('PASSWORD')

sender = os.getenv('SENDER_EMAIL')
subject = "Hello there 🖐"

def generate_bill(filename, content):
    with open(filename, 'wb') as file:
        file.write(str(content).encode())


def send_email(receiver, name, filename):
    content = [f"""\n
                Hello {name} \n
                    Spamming through Python! Bear with me 
                """, filename]
    yag = yagmail.SMTP(user=sender, password=pass_word)
    yag.send(to=receiver, subject=subject, contents=content)

for index, row in df.iterrows():
    try:
        generate_bill(f"{row['name']}.txt", row['amount'])
        send_email(row['email'], row['name'],f"{row['name']}.txt")
    except:
        raise Exception('Unable to send email!')