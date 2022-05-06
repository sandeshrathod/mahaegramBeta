from Crypto.Cipher import AES
import json
import base64
import jwt
import requests
import time
import random


def getTransactionNumber():
    transactionid = []
    for i in range(13):
        transactionid.append(random.randrange(1, 10, 2))
    b = str()
    for i in transactionid:
        b = b + str(i)
    return b
    
data = {
  "iss": "PAYSPRINT",
  "timestamp": round(time.time()),
  "partnerId": 'PS00631',
  "product": "WALLET",
  "reqid": int(getTransactionNumber())
}

payload = {"operator":"11","canumber":"102277100","amount":"100","referenceid":"20018575947","latitude":"27.2232","longitude":"78.26535","mode":"online","bill_fetch":{"billAmount":"820.0","billnetamount":"820.0","billdate":"01Jan1990","dueDate":"2021-01-06","acceptPayment":True,"acceptPartPay":False,"cellNumber":"102277100","userName":"SALMAN"}}

encoded = jwt.encode(data, "UFMwMDYzMTg1NjljMTM5MjAxNWYzYzJlZTM3NzJkZGM1NmMxZjI1", algorithm="HS256")




#import requests
url = "https://paysprint.in/service-api/api/v1/service/bill-payment/bill/paybill"


headers = {
    "Accept": "application/json",
    "Token":encoded,
    "Authorisedkey":"NzEzNmI5ZGNiNGQ2NGYwYjNkYmRjOWEwMzFkY2E0M2U="
}


print("####################################")
response = requests.post(url, json=payload,headers=headers)
print(response.text)

print("####################################")
#print(encoded)
