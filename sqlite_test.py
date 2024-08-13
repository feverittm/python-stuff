import sqlite3 as sl
import pandas as pd

con = sl.connect(":memory:")
cur = con.cursor()

df = pd.read_csv("2023_Team_Roster.csv")
df.to_sql("TEAM", con, if_exists='replace', index=True)

#with con:
#    con.executemany(sql, data)

with con:
    data = con.execute("SELECT * FROM TEAM WHERE ACTIVE=1")
    for row in data:
        print(row)
