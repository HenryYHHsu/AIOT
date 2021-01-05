from pymongo import MongoClient

client = MongoClient(host='127.0.0.1', port=27017)

db = client['test']
#指定集合 
collection = db['member']

mydata = {'name':'henry','phone':'0922333444','email':'test@gmail.com'}


#一次增加一筆
# result= collection.insert_one(mydata)
# print(result.inserted_id)


#一次增加多筆

# mylists = [
#   {'name':'henry1','phone':'0912333444','email':'test1@gmail.com'},
#   {'name':'henry2','phone':'0922333444','email':'test2@gmail.com'},
#   {'name':'henry3','phone':'0932333444','email':'test3@gmail.com'}
# ]

# result= collection.insert_many(mylists)
# print(result.inserted_ids)


#count
#print(collection.count_documents({}))

#delete
# print(collection.delete_one({}))

# print(collection.count_documents({}))

# delete 指定名稱
#print(collection.delete_one({'name':'henry1'}))

# delete 多筆資料
#print(collection.delete_many({'name':'henry'}))

# # 過濾條件
# filter_ = {'name':'henry2'}

# # 要改成什麼資料
# update_ = {"$set":{'name':'poker'}}

# print (collection.update_one(filter_,update_))
# 一樣可以使用 update_many

#查詢所有資料 && sort && limit
result = collection.find().sort('phone',-1).limit(2)

for x in result:
  print(x)
