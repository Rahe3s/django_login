from django import forms  
from login_page.models import User

class UserForm(forms.ModelForm):  
    class Meta:  
        model = User  
        fields = "__all__"  