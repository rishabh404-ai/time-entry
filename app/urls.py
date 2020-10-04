from django.urls import path
from app.views import RegisterView,LogEntryView,UserHistoryListView,index,LoginView,logout

urlpatterns = [
    path('',index),
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('entry/',LogEntryView.as_view()),
    path('history/',UserHistoryListView.as_view()),
    path('logout/',logout)
 
   
]