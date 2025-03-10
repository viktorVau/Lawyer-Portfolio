from rest_framework import serializers
from .models import Lawyer, Service, CaseStudy, BlogPost, ContactRequest

class LawyerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Lawyer
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = '__all__'