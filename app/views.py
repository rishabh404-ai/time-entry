from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from app.forms import RegisterForm, LogEntryForm, LoginForm 
from app.models import LogEntry
from django.contrib.auth.models import User, auth  
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'base.html')

class RegisterView(View):
    template_name = 'register.html'
    form_class = RegisterForm

    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = User.objects.create_user(first_name=cleaned_data['first_name'],last_name=cleaned_data['last_name'],username=cleaned_data['username'],password=cleaned_data['password'],email=cleaned_data['email'])
            user.save()
            auth.login(request,user)
            return redirect('/api/v1/entry/')   
      
        return render(request,self.template_name,{'form':form})    

class LoginView(View): 
    template_name = 'login.html'
    form_class = LoginForm

    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request,self.template_name,{'form':form})
 
    def post(self,request,*args,**kwargs):
        username=self.request.POST['username']
        password=self.request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/api/v1/entry/')    

        else:
            messages.info(request,'Username or Password not maching')    
            return render(request, 'login.html')      

     
    
class LogEntryView(View):
    template_name = 'entry.html'
    form_class = LogEntryForm

    @method_decorator(login_required)
    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request,self.template_name,{'form':form}) 

    @method_decorator(login_required)
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user_id = request.user.id
            entry = LogEntry.objects.create(user_id=user_id,task=cleaned_data['task'],project=cleaned_data['project'],start_time=cleaned_data['start_time'],
                                           end_time=cleaned_data['end_time'],duration=cleaned_data['duration'])

            entry.save()
            return render(request,'tasksubmit.html')    
  
        return render(request,'entry.html',{'form':form})    


class UserHistoryListView(ListView):
    model = LogEntry
    template_name = 'history.html'
    context_object_name = 'entries'
  
    def get_queryset(self):
        return self.model.objects.all().filter(user=self.request.user) 
   
  

def logout(request):
    auth.logout(request)
    return redirect('/api/v1/')