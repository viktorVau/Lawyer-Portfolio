from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

from django.db import models

# Lawyer's Profile
class Lawyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="lawyer_profile")
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)  # Unique identifier
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    address = models.TextField()
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='lawyer_profiles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

# Services Offered by the lawyer
class Service(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name="services")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
# Case Studies or Success Stories
class CaseStudy(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE,  related_name="case_studies")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True, related_name="case_studies")
    title = models.CharField(max_length=255)
    description = models.TextField()
    outcome = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
    

# Blog Post
class BlogPost(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

#FAQ
class FAQ(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name="FAQ")
    question = models.CharField(max_length=500)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

# Contact Requests i.e when a client contacts the lawyer
class ContactRequest(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name="contact_requests")
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.client_email}"
    

