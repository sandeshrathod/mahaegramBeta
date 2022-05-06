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


url = "https://paysprint.in/service-api/api/v1/service/onboard/onboardnew/getonboardurl"

payload = {
    "merchantcode": "1",
    "mobile": "9900990099",
    "is_new": "0",
    "email": "v@gmail.com",
    "firm": "PAYMONEY",
    "callback": "https:mahaegram.com/callbackurl"
}


data = {
  "iss": "PAYSPRINT",
  "timestamp": round(time.time()),
  "partnerId": 'PS00631',
  "product": "WALLET",
  "reqid": int(getTransactionNumber())
}

encoded = jwt.encode(data, "UFMwMDYzMTg1NjljMTM5MjAxNWYzYzJlZTM3NzJkZGM1NmMxZjI1", algorithm="HS256")
print("encode",encoded)
headers = {
    "Accept": "application/json",
    "Token":encoded,
    "Authorisedkey":"NzEzNmI5ZGNiNGQ2NGYwYjNkYmRjOWEwMzFkY2E0M2U="
}


response = requests.post(url, json=payload, headers=headers)


print(response.text)

#jsons = json.loads(response.text)
'''

jwt_options = {
        'verify_signature': True,
        'verify_exp': True,
        'verify_nbf': False,
        'verify_iat': True,
        'verify_aud': False
}

dd = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJ0bmVyaWQiOiIyMDE3NzkzNyIsIm1lcmNoYW50Y29kZSI6IjEiLCJtb2JpbGUiOiI5OTAwOTkwMDk5IiwiaXNfbmV3IjoiMCIsImVtYWlsIjoidkBnbWFpbC5jb20iLCJmaXJtbmFtZSI6IlBBWU1PTkVZIiwicmVxaWQiOiIxNjUxNTc1MjY4NTk5IiwiY2FsbGJhY2siOiJodHRwczpwYXJ0bmVyLmNvbVwvY2FsbGJhY2t1cmwiLCJwaXBlIjoxLCJjdXJyZW50X3RpbWUiOjE2NTE1NzUyNjh9.8Z1VgKKEp0dz8Vwmr8lD0HSKHetRZ0IbYJxnbzsiumU"
d = jwt.decode(dd, "UFMwMDYzMTg1NjljMTM5MjAxNWYzYzJlZTM3NzJkZGM1NmMxZjI1", algorithms=["HS256"],options=jwt_options)
print(d)'''
