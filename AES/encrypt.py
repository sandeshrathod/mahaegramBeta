from Crypto.Cipher import AES
import json
import base64
import jwt
import requests
import time
import random
key = b'1e3b351d2a28471d'
iv = b'27f2333fadc31c1c'
cipher = AES.new(key, AES.MODE_CFB, iv)

'''data = json.dumps({"latitude":12.00,
"longitude":90.00,	
"mobilenumber":27984739827,
"referenceno":342432432432,
"ipaddress":"197.0.0.1",
"adhaarnumber":43234324,
"accessmodetype":"SITE",
"nationalbankidentification":"",	
"requestremarks":"",
"data":"",
"pipe":"",
"timestamp":"2323233",
"transactiontype":"BE",
"submerchantid":1,
"is_iris":"No",
}).encode()

msg =cipher.encrypt(data)


base64_bytes = base64.b64encode(msg)
print(cipher.decrypt(base64_bytes))
base64_string = base64_bytes.decode("ascii")

print(base64_string)'''

#decrypt here

base64_string ='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'
base64_bytes = base64_string.encode("ascii")
#sample_string_bytes = base64.b64decode(base64_bytes)
msg = cipher.decrypt(base64_bytes)
print(msg)






 


#base64_bytes = base64.b64encode(msg)
#print(base64_bytes)



#print(cipher.decrypt(msg))