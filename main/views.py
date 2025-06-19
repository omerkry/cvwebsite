from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def home_view(request):
    return render(request, 'main/home.html')


def about_view(request):
    return render(request, 'main/about.html')


def projects_view(request):
    return render(request, 'main/projects.html')


def skills_view(request):
    return render(request, 'main/skills.html')


def experience_view(request):
    return render(request, 'main/experience.html')


def education_view(request):
    return render(request, 'main/education.html')

def thanks_view(request):
    return render(request, 'main/thanks.html')



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"From: {name} <{email}>\n\n{message}"

            send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})
