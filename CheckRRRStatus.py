import requests
import hashlib


def checkStatus(rrr, b):
    sum = a + b
    return sum

def sha512(input):
    hashed_input = hashlib.sha512(input.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig

merchantId = "2547916"
apiKey = "1946"
rrr = "240008240803"

apiHash = sha512(rrr + apiKey + merchantId)

checkStatus = 'https://demo.remita.net/remita/ecomm/' + merchantId + "/" + rrr + "/" + apiHash + "/status.reg"
# print(checkStatus)
r = requests.get(checkStatus)
print()
print(r.text)
