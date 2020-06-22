from django.contrib import admin
from django.urls import path
from Messaging.views import HomeView
from Messaging.views import ScheduleView
from Messaging.views import ScheduleMessageView
from Messaging.views import BackendView
from Messaging.views import AdminView

urlpatterns = [
    path('', HomeView, name="home"),
    path('schedule/', ScheduleView),
    path('schedule-message/', ScheduleMessageView),
    path('backend/', BackendView),
    path('adminpanel/', AdminView),
    path('admin/', admin.site.urls),
]
