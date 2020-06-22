from datetime import datetime
import time
from celery import Celery
from Messaging.redisHandler import RedisHandler
from Sms.sms import send

app = Celery('tasks',broker="redis://redis:6379/0")

@app.task
def simple_task():
    
    SourceNumber = '07XXXXXXXXX'
    
    Msg = """
            This is your personal reminder. Please log onto www.____.com to view your personal quotes.
        """
    
    MsgQueue = RedisHandler.FetchQueue("All")
    
    while len(MsgQueue) > 0:
        
        print("Items in list: " + str(len(MsgQueue))) 
        
        try:
            status = send(MsgQueue[0][0], SourceNumber, Msg)
            if status == "success":
                RedisHandler.DeleteDB(MsgQueue[0][1] + " " + MsgQueue[0][2])
                RedisHandler.SetDone(MsgQueue[0][1] + " " + MsgQueue[0][2], MsgQueue[0][0])
            else:
                RedisHandler.DeleteDB(MsgQueue[0][1] + " " + MsgQueue[0][2])
                RedisHandler.SetDB(MsgQueue[0][1] + " " + MsgQueue[0][2], MsgQueue[0][0])
        except InvalidDestinationException(e):
            # Store exception in database
            # Get in contact with customer
            print(e)
        except OutOfCreditException(e):
            print(e)
        
        MsgQueue = RedisHandler.FetchQueue("All")