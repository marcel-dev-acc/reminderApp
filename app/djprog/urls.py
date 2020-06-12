from django.contrib import admin
from django.urls import path
from Messaging.views import HomeView
from Messaging.views import ScheduleView
from Messaging.views import Backend
from Messaging.views import AdminView

urlpatterns = [
    path('', HomeView, name="home"),
    path('schedule/', ScheduleView),
    path('backend/', Backend),
    path('adminpanel/', AdminView),
    path('admin/', admin.site.urls),
]
