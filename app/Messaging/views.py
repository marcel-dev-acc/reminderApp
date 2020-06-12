from django.shortcuts import render
from Users.models import AppUser

# Create your views here.
def HomeView(request, *args, **kwargs):
    Context = {
        "numAct": str(12),
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
        return render(request, "schedule.html", {})
    # Login Pathway
    else:
        UserObj = AppUser.objects.get(Username=request.POST.get('username'))
        if request.POST.get('password') == UserObj.Password:
            return render(request, "schedule.html", {})
        # Failed Login Pathway
        else:
            Context = {
                "numAct": str(12),
                "loginSt": "Username / Password not recognised"
            }
            return render(request, "home.html", Context)

def Backend(request, *args, **kwargs):
    return render(request, "backend.html", {})
        
def AdminView(request, *args, **kwargs):
    UserObj = AppUser.objects.get(Username=request.POST.get('username'))
    if request.POST.get('password') == UserObj.Password and UserObj.IsAdmin == True:
        messageList = [["tel1","2020-06-12","13:00","Yes"],["tel2","2020-06-12","13:00","No"]]
        Context = {
            "messageQueue": messageList
        }
        return render(request, "adminpanel.html", Context)
    else:
        Context = {
            "loginSt": "Username / Password not recognised"
        }
        return render(request, "backend.html", Context)