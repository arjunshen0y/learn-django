from django import forms
from emphasis.models import User


class MyNewForm(forms.ModelForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = "__all__"
