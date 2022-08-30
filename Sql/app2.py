import sqlite3
import pandas as pd

con = sqlite3.connect("database.db")
curson = con.cursor()

df = pd.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", con)
print(df)
df.to_csv("db.csv",index=None)