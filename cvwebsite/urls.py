from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import (
    ProjectViewSet,
    SkillViewSet,
    ExperienceViewSet,
    EducationViewSet,
    AboutViewSet,
    ContactMessageViewSet  # ContactMessageViewSet eklendi
)

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'abouts', AboutViewSet)
router.register(r'contactmessages', ContactMessageViewSet)  # ContactMessage rotası eklendi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('main.urls')),
]
