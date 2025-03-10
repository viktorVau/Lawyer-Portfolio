from django.contrib import admin
from .models import Lawyer, Service, CaseStudy, BlogPost, ContactRequest, FAQ

# Change Django Admin Title
admin.site.site_header = "Lawyer Portfolio Admin"
admin.site.site_title = "Lawyer Portfolio"
admin.site.index_title = "Welcome to the Lawyer Portfolio Management"



# Lawyer Admin Customization
@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')  # Displayed columns
    search_fields = ('name', 'email')  # Search by name or email
    list_filter = ('created_at',)  # Filter by date
    ordering = ('-created_at',)  # Order by newest

    def has_module_permission(self, request):
        """Hide the Lawyer model from non-superusers"""
        return request.user.is_superuser



# Service Admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lawyer')
    search_fields = ('title', 'lawyer__name')

# Case Study Admin
@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'lawyer', 'date')
    search_fields = ('title', 'lawyer__name')

# Blog Post Admin
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'lawyer', 'created_at')
    search_fields = ('title', 'lawyer__name')

# Contact Request Admin
@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'lawyer', 'created_at')
    search_fields = ('client_name', 'client_email')
    ordering = ('-created_at',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'lawyer', 'created_at')
    search_fields = ('question', 'lawyer__name')
    ordering = ('-created_at',)
