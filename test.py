import json


data = json.load(open('iot_dev_cert.json'))
print (data['token'], data['dev_id1'])