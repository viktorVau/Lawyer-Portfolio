from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from .models import Lawyer, CaseStudy, Service, BlogPost, ContactRequest, FAQ, Testimonial
from .serializers import LawyerSerializer, ServiceSerializer, CaseStudySerializer, BlogPostSerializer, ContactRequestSerializer, FAQSerializer, TestimonialSerializer
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

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class CaseStudyViewSet(viewsets.ModelViewSet):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact_request = serializer.save()

        lawyer_email = contact_request.lawyer.email
        lawyer_name = contact_request.lawyer.name
        client_name = contact_request.client_name
        client_email = contact_request.client_email
        message = contact_request.message

        # Send mail to lawyer
        lawyer_email_body = f"""
Hello {lawyer_name},

You have received a new service request.

Client Name: {client_name}
Client Email: {client_email}

Message:
{message}

Please response as soon as possible.
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
        
Your request for our services has been recieved.

We will contact you shortly,

Thank you for using our services!

Regards,
{lawyer_name}
"""

        client_email_msg = EmailMessage(
            subject="Service Request Confirmation",
            body=client_email_body,
            from_email=lawyer_email,
            to=[client_email],
            reply_to=[lawyer_email]
        )
        client_email_msg.send(fail_silently=False)

        return Response(serializer.data)
    
