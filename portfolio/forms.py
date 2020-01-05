from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email')
    agreement = forms.BooleanField(label="I agree to the terms and conditions")
