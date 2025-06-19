from django.contrib import admin
from .models import Project, Skill, Experience, Education, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    search_fields = ("title",)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage")
    list_filter = ("percentage",)
    search_fields = ("name",)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "institution", "start_date", "end_date")
    search_fields = ("title", "institution")

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("school_name", "degree", "year")
    search_fields = ("school_name", "degree")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("name", "email")

