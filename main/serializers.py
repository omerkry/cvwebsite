import rest_framework.serializers as serializers
from .models import Project, Skill, Experience, Education, About, ContactMessage  # ContactMessage eklendi

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):  # ContactMessage serializer eklendi
    class Meta:
        model = ContactMessage
        fields = '__all__'
