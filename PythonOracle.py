import oracledb
from pandas import DataFrame
import pandas as pd
import time

date = time.strftime("%Y%m%d_%H%M%S")
connection = oracledb.connect(
    user="",
    password="",
    dsn="")

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

cursor.execute("""



""")


data = cursor.fetchall()

column_names = [desc[0] for desc in cursor.description]

connection.close()

df = pd.DataFrame(data, columns=column_names)

output_file = f'Name_{date}.xlsx'
df.to_excel(output_file, index=False)

print(f"Data exported to {output_file}")
