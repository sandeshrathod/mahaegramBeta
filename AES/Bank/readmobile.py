import pandas as pd
import json
df = pd.read_excel('DMT-BANK-LIST.xlsx')
#
count = 0

arr = []
for i in df["BANK NAME"]:
    arr.append({"id":str(df["BANKID"][count]),"BankName":str(i)})
    count = count + 1

print(arr)