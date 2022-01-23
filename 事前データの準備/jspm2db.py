import json
import sqlite3
import time
import datetime

DB_FILE = "data.db"
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute('create table if not exists expart ("timestampMs","year","mon","day","hour","min","sec", "latitudeE7","longitudeE7")')
#c.execute('create table table_name (timestampMs,latitudeE7,longitudeE7)')

json_open=open("ロケーション履歴.json","r")
json_load=json.load(json_open)
for i in json_load["locations"]:
    data = list()
    epoch_time = int(i["timestampMs"])/1000
    dt = time.localtime(epoch_time)
    data.append(int(epoch_time))
    data.append(dt[0])
    data.append(dt[1])
    data.append(dt[2])
    data.append(dt[3])
    data.append(dt[4])
    data.append(dt[5])
    data.append(i["latitudeE7"]/10000000)
    data.append(i["longitudeE7"]/10000000)
    c.execute('insert into expart values (?,?,?,?,?,?,?,?,?)', data)
    #print(i["timestampMs"])
    ###print("/")
    
#print(json_load)




conn.commit()
c.close()