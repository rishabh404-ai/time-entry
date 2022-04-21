from django.conf import settings
import csv
from re import I
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from app.forms import RegisterForm, LogEntryForm, LoginForm
from app.models import LogEntry
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.contrib import messages
import time

import pyscreenshot as ImageGrab
import schedule
import pyautogui
from datetime import datetime
# Create your views here.


def index(request):
    return render(request, 'base.html')


class RegisterView(View):
    template_name = 'register.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = User.objects.create_user(first_name=cleaned_data['first_name'], last_name=cleaned_data['last_name'],
                                            username=cleaned_data['username'], password=cleaned_data['password'], email=cleaned_data['email'])
            user.save()
            auth.login(request, user)
            return redirect('/entry/')

        return render(request, self.template_name, {'form': form})


def startrecord(request):
    return render(request, 'record.html')


def CaptureScreenShot(request):
    if request.user.is_authenticated:
        print(request.user.id)

        def take_screenshot():
            print("Taking screenshot...")

            image_name = "screenshot-{}".format(str(datetime.now()))
            screenshot = pyautogui.screenshot()

            filepathloc = "/Users/rishabhm404/Desktop/screenshots/{}.png".format(
                image_name)

            screenshot.save(filepathloc)

            print("Screenshot taken...")

            return filepathloc

        def main():
            schedule.every(5).seconds.do(take_screenshot)

            while True:
                schedule.run_pending()
                time.sleep(1)

        main()
    else:
        return redirect('/start-recording/')


class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/entry/')

        else:
            messages.info(request, 'Username or Password not maching')
            return render(request, 'login.html')


class LogEntryView(View):
    template_name = 'entry.html'
    form_class = LogEntryForm

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user_id = request.user.id
            entry = LogEntry.objects.create(user_id=user_id, task=cleaned_data['task'], project=cleaned_data['project'], start_time=cleaned_data['start_time'],
                                            end_time=cleaned_data['end_time'], duration=cleaned_data['duration'])

            entry.save()
            return render(request, 'tasksubmit.html')

        return render(request, 'entry.html', {'form': form})


class UserHistoryListView(ListView):
    model = LogEntry
    template_name = 'history.html'
    context_object_name = 'entries'

    def get_queryset(self):
        return self.model.objects.all().filter(user=self.request.user)


def logout(request):
    auth.logout(request)
    return redirect('/home/')


class ExportCsv(ListView):
    model = LogEntry
    template_name = 'download-csv.html'
    context_object_name = 'entries'

    def get_queryset(self):
        return None


def exportcsvperuser(request):
    entries = LogEntry.objects.filter(user=request.user)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={request.user.username}-data.csv'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Task', 'Project',
                    'Start Time', 'End Time', 'Total Duration Of Work'])
    time_entries = entries.values_list(
        'user__username', 'task', 'project', 'start_time', 'end_time', 'duration')
    for entry in time_entries:
        writer.writerow(entry)
    return response


def exportcsv(request):
    entries = LogEntry.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=employees-data.csv'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Task', 'Project',
                    'Start Time', 'End Time', 'Total Duration Of Work'])
    time_entries = entries.values_list(
        'user__username', 'task', 'project', 'start_time', 'end_time', 'duration')
    for entry in time_entries:
        writer.writerow(entry)
    return response


def CaptureScreenShot(request):
    if request.user.is_authenticated:
        print(request.user.id)

        def take_screenshot():
            print("Taking screenshot...")

            image_name = "screenshot-{}.png".format(str(datetime.now()))
            screenshot = pyautogui.screenshot()

            filepathloc = settings.MEDIA_ROOT/image_name

            screenshot.save(filepathloc)

            print("Screenshot taken...")

            return filepathloc

        def main():
            if request.user.is_authenticated:

                schedule.every(5).seconds.do(take_screenshot)

                while True:
                    if request.user.is_authenticated:
                        schedule.run_pending()
                        time.sleep(1)
                    else:
                        break
            else:

                return redirect('/start-recording/')

        main()
    else:
        return redirect('/start-recording/')
