import requests
import json


# 作業1 : 練習使用一個民生物聯網 API，例如空氣、地震等感測站所回傳的紀錄資料。
# api request 中央氣象局地震監測站 SensorThings API 服務網址 
r = requests.get("https://sta.ci.taiwan.gov.tw/STA_Earthquake_v2/v1.0/Things")

result_1 = json.loads(r.text)
raw_data_q1 =  result_1['value']


# 作業2 : 練習操作 OGC SensorThings API，將環保局測站位置的資料抓取下來，並且觀察下載資料的內容。

r_q2 = requests.get("https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Things")

result_2 = json.loads(r_q2.text)
raw_data_q2 =  result_2['value']



# 作業3 : 
# 依據作業 2 所下載的各個環保局測站感測器的描述資料，進一步點選 Datastreams、Locations，
# 以及 Datastreams 點選進入後，點選 Observations 的 URL，觀察所下載到的資料內容，其中 Observations 內部是否包含個別感測器紀錄的資料。

# 以第一筆資料為例

raw_data_q3 = raw_data_q2[0]


# 取得 "Datastreams@iot.navigationLink" 

stream = raw_data_q3["Datastreams@iot.navigationLink"]

# 可透過取得 stream endpoint 打API獲取資訊

print (stream)

# 取得 "Locations@iot.navigationLink"

location = raw_data_q3["Locations@iot.navigationLink"]

# 可透過取得 location endpoint 打API獲取資訊

print(location)









