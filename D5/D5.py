import requests
import json

# api request 中央氣象局地震監測站 SensorThings API 服務網址 
r = requests.get("https://sta.ci.taiwan.gov.tw/STA_Earthquake_v2/v1.0/Things")

result = json.loads(r.text)
raw_data =  result['value']


print(len(raw_data))




