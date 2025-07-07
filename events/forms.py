from django import forms


class TempPaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16, min_length=16)
