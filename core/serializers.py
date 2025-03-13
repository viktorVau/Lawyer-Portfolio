from rest_framework import serializers
from .models import Lawyer, Service, Experience,CaseStudy, ContactRequest, FAQ, Testimonial

class LawyerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Lawyer
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class CaseStudySerializer(serializers.ModelSerializer):
    service = serializers.SlugRelatedField(
        queryset = Service.objects.all(),
        slug_field ='title'
    )

    class Meta:
        model = CaseStudy
        fields = '__all__'

# class BlogPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BlogPost
#         fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class ContactRequestSerializer(serializers.ModelSerializer):
    lawyer = serializers.PrimaryKeyRelatedField(read_only=True)  # Lawyer is auto-assigned

    class Meta:
        model = ContactRequest
        fields = ["id", "lawyer", "name", "email", "phone", "message", "created_at"]

