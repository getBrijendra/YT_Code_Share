import jwt
import datetime
import json

#[header].[payload].[signature]

payload = {"sub": "admin", "name": "Anicca" ,"exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)}
secret = "bkanicca_secret"

token = jwt.encode(payload, secret, algorithm="HS256")

print(token)

# Decode a JWT and print the subject claim
decoded = jwt.decode(token, secret, algorithms=["HS256"])

print(decoded)  # "admin"
