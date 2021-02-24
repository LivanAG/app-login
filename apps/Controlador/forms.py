from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm (AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['placeholder'] = i.name
            i.field.widget.attrs['autocomplete'] = 'off' 


