# time-entry

Assignment For @Ufaber

Heroku Web Hosting Link - https://timeentryapi.herokuapp.com/api/v1/

Features Listed In The App :

● As a user, I should be able to register with my name, username, email, etc.

● As a user, I should be able to log my time entries for a task with the following fields.
          ○ Input field to enter task name.
          ○ A dropdown to choose the project that I am working on.
          ○ Start time and end time.
          ○ A timer which I can start to track time for a task.
          
● As a user, I should be able to browse through my time entries of previous days.

● No other features are required.

● Time entries should be saved in the database.


- PROJECT FOLDER > TimeEntry
- App > app

1. Landing Page Endpoint :
Hosting > https://timeentryapi.herokuapp.com/api/v1/
Localhost > http://127.0.0.1:8000/api/v1/

2. Registeration Page Endpoint :
Hosting > https://timeentryapi.herokuapp.com/api/v1/register/
Localhost > http://127.0.0.1:8000/api/v1/register/

3. Login Page Endpoint :
Hosting > https://timeentryapi.herokuapp.com/api/v1/login/
Localhost > http://127.0.0.1:8000/api/v1/login/

4. Task Creation Endpoint (After Login or Registration) :
Hosting > https://timeentryapi.herokuapp.com/api/v1/entry/
Localhost > http://127.0.0.1:8000/api/v1/entry/

5. User Tasks History Endoint:
Hosting > https://timeentryapi.herokuapp.com/api/v1/history/
Localhost > http://127.0.0.1:8000/api/v1/history/


How to get the app running locally ?

For Linux : RUN > pip3 install -r requirements.txt & python3 manage.py runserver

For Windows : RUN > pip install -r requirements.txt & python manage.py runserver
