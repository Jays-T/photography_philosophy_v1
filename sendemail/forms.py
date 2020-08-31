from django import forms


class ContactForm(forms.Form):
    your_email = forms.EmailField(max_length=254, required=True)
    subject = forms.CharField(max_length=60, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    placeholders = {
        'your_email': 'Your Email',
        'subject': 'Subject',
        'message': 'Message',
    }

    self.fields['your_email'].widget.attrs['autofocus'] = True
    for field in self.fields:
        placeholder = placeholders[field]
    self.fields[field].widget.attrs['placeholder'] = placeholder
