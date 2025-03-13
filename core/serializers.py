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
    lawyer_email = serializers.EmailField(write_only=True)  # Accepts lawyer's email

    class Meta:
        model = ContactRequest
        fields = ["id", "name", "email", "phone", "message", "created_at", "lawyer_email"]
        read_only_fields = ["created_at"]

    def create(self, validated_data):
        lawyer_email = validated_data.pop("lawyer_email", None)
        
        if not lawyer_email:
            raise serializers.ValidationError({"lawyer_email": "This field is required."})

        try:
            lawyer = Lawyer.objects.get(email=lawyer_email)
        except Lawyer.DoesNotExist:
            raise serializers.ValidationError({"lawyer_email": "Lawyer not found."})

        validated_data["lawyer"] = lawyer  # Assign the lawyer object
        return super().create(validated_data)

