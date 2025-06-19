from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    subject = forms.CharField(label='Subject', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Your message'}))
