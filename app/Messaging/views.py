from django.shortcuts import render
from Users.models import AppUser
from Messaging.redisHandler import RedisHandler
from datetime import datetime

# Create your views here.
def HomeView(request, *args, **kwargs):
    LoginHist = RedisHandler.FetchQueue("LoginHist")
    Context = {
        "numAct": str(len(LoginHist)),
        "loginSt": ""
    }
    return render(request, "home.html", Context)
    
def ScheduleView(request, *args, **kwargs):
    # user Creation Pathway
    if request.POST.get('type') == "C":
        AppUser.objects.create(
            Username = request.POST.get('fname') + request.POST.get('lname'),
            Password = request.POST.get('password'),
            Fname = request.POST.get('fname'),
            Lname = request.POST.get('lname'),
            PhoneNumber = request.POST.get('tel'),
        )
        Context = {
            "userFname": request.POST.get('fname'),
            "tel": request.POST.get('tel'),
            "msgQueue": ""
        }
        RedisHandler.SetDB("UserLogin", "", request.POST.get('tel'))
        return render(request, "schedule.html", Context)
    # Login Pathway
    else:
        UserObj = AppUser.objects.get(Username=request.POST.get('username'))
        if request.POST.get('password') == UserObj.Password:
            MsgQueue = RedisHandler.FetchQueue(UserObj.PhoneNumber)
            Context = {
                "userFname": UserObj.Fname,
                "tel": UserObj.PhoneNumber,
                "msgQueue": MsgQueue
            }
            RedisHandler.SetDB("UserLogin", "", UserObj.PhoneNumber)
            return render(request, "schedule.html", Context)
        # Failed Login Pathway
        else:
            Context = {
                "numAct": str(12),
                "loginSt": "Username / Password not recognised"
            }
            return render(request, "home.html", Context)

def ScheduleMessageView(request, *args, **kwargs):
    Key = request.POST.get('date') + " " + request.POST.get('time')
    Value = request.POST.get('tel')
    UserObj = AppUser.objects.get(PhoneNumber=Value)
    RedisHandler.SetDB("Message", Key, Value)
    MsgQueue = RedisHandler.FetchQueue(UserObj.PhoneNumber)
    Context = {
        "userFname": UserObj.Fname,
        "tel": UserObj.PhoneNumber,
        "msgQueue": MsgQueue
    }
    return render(request, "schedule.html", Context)

def BackendView(request, *args, **kwargs):
    return render(request, "backend.html", {})
        
def AdminView(request, *args, **kwargs):
    UserObj = AppUser.objects.get(Username=request.POST.get('username'))
    if request.POST.get('password') == UserObj.Password and UserObj.IsAdmin == True:
        MsgQueue = RedisHandler.FetchQueue("All")
        Context = {
            "msgQueue": MsgQueue
        }
        return render(request, "adminpanel.html", Context)
    else:
        Context = {
            "loginSt": "Username / Password not recognised"
        }
        return render(request, "backend.html", Context)
