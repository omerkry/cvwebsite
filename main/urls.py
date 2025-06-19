from django.urls import path
from .views import (
    home_view,
    about_view,
    projects_view,
    skills_view,
    experience_view,
    education_view,
    contact_view,
    thanks_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('projects/', projects_view, name='projects'),
    path('skills/', skills_view, name='skills'),
    path('experience/', experience_view, name='experience'),
    path('education/', education_view, name='education'),
    path('contact/', contact_view, name='contact'),
path('thanks/', thanks_view, name='thanks'),
]
