from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://savva:111@localhost:5432/mydatabase')


df = pd.read_sql('message',con=engine)

print(df[["id","is_read"]])


list = ['a','s','a','v',]

storka = ''.join(list)
print(storka)