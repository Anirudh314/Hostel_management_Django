from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from accounts.models import room_form
from django.core.validators import RegexValidator

#New form for room booking
class room_form1(ModelForm):
    usn = forms.CharField(max_length=10 , validators=[RegexValidator('^4[Jj][Cc]1[0-9][a-zA-Z]{2}[0-9]{3}')])
    room_no = forms.CharField(max_length=4 , validators=[RegexValidator('^[a-zA-Z]-[0-9]+')])
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)
    
    class Meta:
        model = room_form        
        fields=(
            'usn',
            'room_no',
            'name',
            'email',
        )

    def save(self, commit=True):
        room_form = super(room_form1, self).save(commit=False)
        room_form.usn = self.cleaned_data['usn']
        room_form.room_no = self.cleaned_data['room_no']
        room_form.name = self.cleaned_data['name']
        room_form.email = self.cleaned_data['email']
        
        if(commit):
            room_form.save()

        return room_form
        

class UserRegistrationForm(forms.Form):
    
   # username.widget.attrs.update({'id' : 'form-control'})

    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )

    

    
   # email.widget.attrs.update({'id' : 'form-control'})
    password1 = forms.CharField(
        required = True,
        label = 'Password1',
        max_length = 32,
        widget = forms.PasswordInput()
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    
