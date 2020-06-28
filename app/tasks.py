from datetime import datetime, timedelta
import time
from celery import Celery
from Messaging.redisHandler import RedisHandler
from Sms.sms import send

DayLightSavings = True
app = Celery('tasks',broker="redis://redis:6379/0")

@app.task
def simple_task():    
    
    #RedisHandler.PureQueue()
    print("Celery Worker Running")
    
    SourceNumber = '07XXXXXXXXX'
    
    Msg = """
            This is your personal reminder. Please log onto www.____.com to view your personal quotes.
        """
    
    MsgQueue = RedisHandler.FetchQueue("All")
    #print(MsgQueue)
    
    exit_this = False
    while len(MsgQueue) > 0 and exit_this == False:
        
        #print("Items in list: " + str(len(MsgQueue))) 
        
        for TaskValue in MsgQueue:
            Key = TaskValue[1] + " " + TaskValue[2] + " " + TaskValue[0]
            #print(Key)
            
            if DayLightSavings == True:
                TimeDifference = 1
            else:
                TimeDifference = 0
            Now = datetime.now() + timedelta(hours=TimeDifference)
            NowDate = str(Now)[0:10]
            NowTime = str(Now)[11:16]
            
            # Get the task rows date time combo
            TaskYear = int(TaskValue[1][0:4])
            TaskMonth = int(TaskValue[1][5:7])
            TaskDay = int(TaskValue[1][8:10])
            TaskHour = int(TaskValue[2][0:2])
            TaskMin = int(TaskValue[2][3:5])
            TaskDateTime = datetime(TaskYear, TaskMonth, TaskDay,
                                    TaskHour, TaskMin)
            
            if TaskValue[1] == NowDate and TaskValue[2] == NowTime:

                if TaskValue[3] == "No":
                    try:
                        status = send(TaskValue[0], SourceNumber, Msg)
                        if status == "success":
                            RedisHandler.DeleteDB(Key)
                            RedisHandler.SetDone(Key, TaskValue[0])
                        else:
                            NowInsert = Now + timedelta(hours=1)
                            NowInsertDate = str(Now)[0:10]
                            NowInsertTime = str(Now)[11:16]
                            Key = NowInsertDate + " " + NowInsertTime + " " + TaskValue[0]
                            RedisHandler.DeleteDB(Key)
                            RedisHandler.SetDB("Message", Key, Value)
                    
                    except InvalidDestinationException(e):
                        # Store exception in database
                        # Get in contact with customer
                        print(e)
                    
                    except OutOfCreditException(e):
                        print(e)
                        NowInsert = Now + timedelta(hours=1)
                        NowInsertDate = str(Now)[0:10]
                        NowInsertTime = str(Now)[11:16]
                        Key = NowInsertDate + " " + NowInsertTime + " " + TaskValue[0]
                        RedisHandler.DeleteDB(Key)
                        RedisHandler.SetDB("Message", Key, Value)

            elif TaskDateTime < Now:
            
                if TaskValue[3] == "No":
                    RedisHandler.DeleteDB(Key)
                    RedisHandler.SetSkip(Key, TaskValue[0])

        
        MsgQueue = RedisHandler.FetchQueue("All")
        #exit_this = True
        
        print("Sleeping")
        time.sleep(10)
        
    print("Celery Worker Finished")
