from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Create your models here.

# Lawyer's Profile
class Lawyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="lawyer_profile")
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)  # Unique identifier
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    address = models.TextField()
    title = models.CharField(max_length=255, null=True)
    slogan = models.CharField(max_length=255, null= True)
    bio = models.TextField()
    tagline = models.CharField(max_length=255, null=True)
    education = models.CharField(max_length=255, null=True)
    bar_membership = models.CharField(max_length=255, null= True)
    certification = models.CharField(max_length=255, null=True)
    profile_image = models.ImageField(upload_to='lawyer_profiles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Experience(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='experience')
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_year = models.CharField(max_length=4, null=True)
    end_year = models.CharField(blank=True, null=True, max_length=10)
    # is_current = models.BooleanField(default=False)
    responsibilities = models.TextField()

    def __str__(self):   
        return f"{self.title} at {self.company} ({self.start_year} - {self.end_year})"

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
# class BlogPost(models.Model):
#     lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name="blog_posts")
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField()

#     def __str__(self):
#         return self.title

# User = get_user_model()

class Testimonial(models.Model):
    lawyer = models.ForeignKey('Lawyer', on_delete=models.CASCADE, related_name='testimonials')
    client_name = models.CharField(max_length=255)
    client_position = models.CharField(max_length=255, blank=True, null=True)  # Optional
    rating = models.IntegerField(choices=[(i, f"{i} Stars") for i in range(1, 6)], default=5)
    testimonial = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.lawyer.name}"

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
    

