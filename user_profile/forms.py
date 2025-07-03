from django import forms


class UpdateNameForm(forms.Form):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
