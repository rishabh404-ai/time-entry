from django.urls import path
from app.views import *

urlpatterns = [
    path('home/', index),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('entry/', LogEntryView.as_view()),
    path('history/', UserHistoryListView.as_view()),
    path('logout/', logout),
    path('download-employee-data/', ExportCsv.as_view()),
    path('get-csv-employee-data/', exportcsv),
    path('per-user-get-csv-employee-data/', exportcsvperuser),
    path('record/', CaptureScreenShot),
    path('start-recording/', startrecord)



]
