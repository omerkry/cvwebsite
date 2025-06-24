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
from django.conf import settings
from django.conf.urls.static import static

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
