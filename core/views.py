from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lawyer, CaseStudy,Service, ContactRequest, FAQ, Testimonial, Experience
from .serializers import LawyerSerializer, ServiceSerializer, CaseStudySerializer, ContactRequestSerializer, FAQSerializer, TestimonialSerializer, ExperienceSerializer
from django.shortcuts import redirect
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

# def create_superuser():
#     try:
#         if not User.objects.filter(username="admin").exists():
#             User.objects.create_superuser("admin", "admin@example.com", "AdminPassword123")
#             print("Superuser created successfully!")
#         else:
#             print("Superuser already exists!")
#     except IntegrityError:
#         print("Superuser already exists!")

# create_superuser()

def homepage_redirect(request):
    return redirect("/admin/")  # Redirects to Django Admin

class LawyerDetailView(generics.RetrieveAPIView):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer
    lookup_field = "slug"

class LawyerViewSet(viewsets.ModelViewSet):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class CaseStudyViewSet(viewsets.ModelViewSet):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer

# class BlogPostViewSet(viewsets.ModelViewSet):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class ContactRequestViewSet(viewsets.ModelViewSet):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

    
    def create(self, request, *args, **kwargs):
        # Get the lawyer from the database (assuming there is only one lawyer)
        lawyer = Lawyer.objects.first()
        if not lawyer:
            return Response({"error": "No lawyer found in the database."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a mutable copy of request.data and add lawyer ID
        mutable_data = request.data.copy()
        mutable_data["lawyer"] = lawyer.id  # Assign the lawyer automatically

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(lawyer=lawyer)  # Save with lawyer


        # Email notifications (same as before)
        lawyer_email = lawyer.email
        lawyer_name = lawyer.name
        client_name = contact_request.name
        client_email = contact_request.email
        client_phone = contact_request.phone
        message = contact_request.message

        # Send mail to lawyer
        lawyer_email_body = f"""
Hello {lawyer_name},

You have received a new service request.

Client Name: {client_name}
Client Email: {client_email}
Client Phone Number: {client_phone}

Message:
{message}

Please respond as soon as possible.
"""

        lawyer_email_msg = EmailMessage(
            subject=f"New Service Request from {client_name}",
            body=lawyer_email_body,
            from_email=settings.EMAIL_HOST_USER,
            to=[lawyer_email],
            reply_to=[client_email],
        )
        lawyer_email_msg.send(fail_silently=False)

        # Send confirmation email to client
        client_email_body = f"""
Dear {client_name},
        
Your request for our services has been received.

We will contact you shortly.

Thank you for using our services!

Regards,
{lawyer_name}
"""

        client_email_msg = EmailMessage(
            subject="Service Request Confirmation",
            body=client_email_body,
            from_email=settings.EMAIL_HOST_USER,
            to=[client_email],
            reply_to=[lawyer_email]
        )
        client_email_msg.send(fail_silently=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
