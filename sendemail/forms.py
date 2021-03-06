from django import forms


class ContactForm(forms.Form):
    your_email = forms.EmailField(max_length=254, required=True)
    subject = forms.CharField(max_length=60, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
