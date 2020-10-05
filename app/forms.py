from django import forms
from django.contrib.auth.models import User, auth
from .models import LogEntry
from django.forms import TextInput

class RegisterForm(forms.ModelForm):
    
    password2 = forms.CharField(max_length=8,required=True,widget=forms.TextInput(attrs={'type':'password','class':"form-control",'placeholder':"Confirm your Password", 'name':"message" ,'required':'required'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','password2']
        
        widgets ={'first_name': TextInput(attrs={'type':'text','class':"form-control", 'placeholder':"Enter your First Name", 'name':"first_name" ,'required':'required'}),
                  'last_name': TextInput(attrs={'type':'text','class':"form-control", 'placeholder':"Enter your Last Name", 'name':"last_name" ,'required':'required'}),
                  'username': TextInput(attrs={'type':'text','class':"form-control",'placeholder':"Enter your Username", 'name':"username" }),
                  'email':TextInput(attrs={'type':'email','class':"form-control",'placeholder':"Enter your Email", 'name':"email" ,'required':'required'}),
                  'password':TextInput(attrs={'type':'password','class':"form-control",'placeholder':"Create your Password", 'name':"password" ,'required':'required'}),
               
        } 

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')   

        if password!=password2:
            raise forms.ValidationError('Failed :Password not matching')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Failed : Email is already taken')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Failed : Username is already taken')
  
        if not username:
            raise forms.ValidationError('Failed : Please enter username')

        if not email:
            raise forms.ValidationError('Failed : Please enter email')

        if not first_name:
            raise forms.ValidationError('Failed : Please enter first name')

        if not last_name:
            raise forms.ValidationError('Failed : Please enter last name') 


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'type':'text','class':"form-control",'placeholder':"Enter your Username", 'name':"username" }))
    password = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'type':'password','class':"form-control",'placeholder':"Create your Password", 'name':"password" ,'required':'required'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
        else:
           raise forms.ValidationError('Username or Password not maching') 


class LogEntryForm(forms.ModelForm):

    PROJECT_CHOICES =( 
        ("1", "Web Development"), 
        ("2", "Software Development"), 
        ("3", "Machine Learning"), 
        ("4", "Deep Learning"), 
        ("5", "Natural Language Processing"), 
    ) 
    
    project = forms.ChoiceField(label='Select Your Desired Project',choices=PROJECT_CHOICES,widget=forms.Select(attrs={"name": "select_0","class": "form-control"}))
   
    class Meta:
        model = LogEntry
        fields = ['task','project','start_time','end_time','duration']
        widgets = {
            'task':TextInput(attrs={'type':'text','class':"form-control", 'placeholder':"Enter your Task", 'name':"task" ,'required':'required'}),
            'start_time':TextInput(attrs={'type':'datetime-local','class':"form-control", 'placeholder':"Add your task start date", 'name':"start_time" ,'required':'required'}),
            'end_time':TextInput(attrs={'type':'datetime-local','class':"form-control", 'placeholder':"Add your task end date", 'name':"end_time" ,'required':'required'}),
            'duration': TextInput(attrs={'type':'duration','class':"form-control", 'placeholder':"Enter your Duration as per the track time like 13:50:23 ", 'name':"duration" ,'required':'required'})
        }
  
    def clean(self):
        cleaned_data = super().clean()
        task = cleaned_data.get('task')
        project = cleaned_data.get('project')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        duration = cleaned_data.get('duration')    


        if not task:
            raise forms.ValidationError('Failed : Please enter your task') 

        if not project:
            raise forms.ValidationError('Failed : Please enter your project') 

        if not start_time:
            raise forms.ValidationError('Failed : Please enter your start time') 

        if not end_time:
            raise forms.ValidationError('Failed : Please enter your end time')     
