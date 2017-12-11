from ubidots import ApiClient
import json


data = json.load(open('iot_dev_cert.json'))
# print (data['token'], data['dev_id1'])

api = ApiClient(token=data['token'])
temperature = api.get_variable(data['dev_id1'])


# To read 1 value
# last_value = temperature.get_values(1)
# print ("temp = %d" %(last_value[0]['value']))

last_values = temperature.get_values()
print ("len = %d,  Temp Val = %d "%(len(last_values),last_values[0]['value']))

for i in range(20,90,10):
    # temperature.save_value({'value': i})
    print ("input = %d " %(i))