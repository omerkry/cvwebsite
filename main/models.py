from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField(help_text="Yüzdelik beceri seviyesi (0-100)")

    def __str__(self):
        return f"{self.name} - {self.percentage}%"


class Experience(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True, help_text="Hâlâ devam ediyorsa boş bırakılabilir.")
    description = models.TextField()

    def __str__(self):
        return f"{self.title} – {self.institution}"


class Education(models.Model):
    school_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.school_name} – {self.degree}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"

