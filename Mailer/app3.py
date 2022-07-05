from dotenv import load_dotenv
import os 
import pandas as pd
import yagmail

load_dotenv()

sender = os.getenv("SENDER_EMAIL")
pass_word = os.getenv("PASSWORD")

subject = "Hello there 🖐"
df = pd.read_csv("./emais.csv")


def send_email(receiver, content):
    yag = yagmail.SMTP(user=sender, password=pass_word)
    yag.send(to=receiver, subject=subject, contents=content)
    print("LMAO SPAMMED")

for index, row in df.iterrows():
    content = f"Hello there {row['name']}"
    send_email(row['email'], content)