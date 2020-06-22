import redis
from datetime import datetime, timedelta
import json

r = redis.Redis(host='redis', port=6379, db=0)

class RedisHandler:

    def SetDB(Type, Key,Value):
        if Type == "UserLogin":
            Now = datetime.now()
            UserLogin = "UL:" + str(Now.year) + "-" +  str(Now.month)
            UserLogin = UserLogin + "-" + str(Now.day) + " "
            UserLogin = UserLogin + str(Now.hour) + ":"
            UserLogin = UserLogin + str(Now.minute)
            r.set(UserLogin, Value)
        else:
            Value = {
                "tel": Value,
                "sent": "No"
            }
            Value = json.dumps(Value)
            r.set(Key, Value)
            
    def SetDone(Key, Value):
        Value = {
            "tel": Value,
            "sent": "Yes"
        }
        Value = json.dumps(Value)
        r.set(Key, Value)
        
    def GetDB(Key):
        return r.get(Key)
        
    def DeleteDB(Key):
        r.delete(Key)
        return Key + " Deleted"
        
    def FetchQueue(Type):
        Now = datetime.now()
        Year0 = Now.year
        Year1 = Year0 + 1
        DataArray = []
        if Type == "All":
            # Fetch All Pending Messages
            for Item in r.scan_iter():
                Key = Item.decode("utf-8")
                if Key[0:4] == str(Year0) or Key[0:4] == str(Year1):
                    Value = r.get(Key)
                    DateTime = Key.split(" ")
                    Value = r.get(Key)
                    Value = Value.decode("utf-8")
                    Value = json.loads(Value)
                    DataArray.append([Value['tel'], DateTime[0], 
                                    DateTime[1], Value['sent']])
                                    
        elif Type[0:1] == "0":
            # Fetch Specific Pending Messages
            for Item in r.scan_iter():
                Key = Item.decode("utf-8")
                if Key[0:4] == str(Year0) or Key[0:4] == str(Year1):
                    DateTime = Key.split(" ")
                    Value = r.get(Key)
                    Value = Value.decode("utf-8")
                    Value = json.loads(Value)
                    if Value['tel'] == Type:
                        DataArray.append([Value['tel'], DateTime[0], 
                                        DateTime[1], Value['sent']])
                                        
        else:
            # Fetch User Login History
            for Item in r.scan_iter():
                Key = Item.decode("utf-8")
                if Key[0:3] == "UL:":
                    LoginStamp = Key[Key.find(":") + 1 :len(Key)]
                    LoginPair = LoginStamp.split(" ")
                    DateTriple = LoginPair[0].split("-")
                    TimePair = LoginPair[1].split(":")
                    LoginDateTime = datetime(int(DateTriple[0]),
                                        int(DateTriple[1]),
                                        int(DateTriple[2]),
                                        int(TimePair[0]),
                                        int(TimePair[1])
                                    )
                    LoginWindow = Now - timedelta(minutes=20)
                    if LoginDateTime >= LoginWindow:
                        DataArray.append(Key)
        return DataArray