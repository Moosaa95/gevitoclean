from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=200)
    subject = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)



class QuoteForm(forms.Form):
    name = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=200)
    type = forms.CharField(max_length=200)
    service = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    # message = forms.CharField(widget=forms.Textarea)



