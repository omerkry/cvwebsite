from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Project, About, Skill, Experience, Education, ContactMessage  # ContactMessage eklendi

from rest_framework import viewsets
from .serializers import (
    ProjectSerializer,
    SkillSerializer,
    ExperienceSerializer,
    EducationSerializer,
    AboutSerializer,
    ContactMessageSerializer,  # ContactMessageSerializer eklendi
)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):  # ContactMessage ViewSet eklendi
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

# Diğer view fonksiyonları değişmedi
def home_view(request):
    return render(request, 'main/home.html')

def about_view(request):
    about = About.objects.first()
    return render(request, 'main/about.html', {'about': about})

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

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
