from django import forms


class PaymentForm(forms.Form):
    cardholder_name = forms.CharField(max_length=50)
