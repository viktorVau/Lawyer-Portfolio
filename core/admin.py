from django.contrib import admin
from .models import Lawyer, Service, CaseStudy, ContactRequest, Testimonial, FAQ, Experience

# Change Django Admin Title
admin.site.site_header = "Lawyer Portfolio Admin"
admin.site.site_title = "Lawyer Portfolio"
admin.site.index_title = "Welcome to the Lawyer Portfolio Management"



# Lawyer Admin Customization (Only visible to Superusers)
@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers see all lawyers
        return qs.filter(user=request.user)  # Staff users only see their lawyer

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.user:
            return True  # Staff users can edit only their lawyer profile
        return request.user.is_superuser  # Superusers can edit all lawyers

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # Only superusers can delete
# @admin.register(Lawyer)
# class LawyerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'created_at')
#     search_fields = ('name', 'email')
#     list_filter = ('created_at',)
#     ordering = ('-created_at',)

    # def has_module_permission(self, request):
    #     """Only superusers can see the Lawyer model in the admin panel."""
    #     return request.user.is_superuser

    # def has_view_permission(self, request, obj=None):
    #     """Only superusers can view lawyers."""
    #     return request.user.is_superuser

    # def has_add_permission(self, request):
    #     """Only superusers can add lawyers."""
    #     return request.user.is_superuser

    # def has_change_permission(self, request, obj=None):
    #     """Only superusers can edit lawyers."""
    #     return request.user.is_superuser

    # def has_delete_permission(self, request, obj=None):
    #     """Only superusers can delete lawyers."""
    #     return request.user.is_superuser



# Service Admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lawyer')
    search_fields = ('title', 'lawyer__name')
    

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_year', 'end_year', 'lawyer')
    search_fields = ('title', 'lawyer__name')


# Case Study Admin
@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'lawyer', 'date')
    search_fields = ('title', 'lawyer__name')

# Blog Post Admin
# @admin.register(BlogPost)
# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'lawyer', 'created_at')
#     search_fields = ('title', 'lawyer__name')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'lawyer', 'rating', 'created_at')
    search_fields = ('client_name', 'lawyer__name')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'lawyer', 'created_at')
    search_fields = ('question', 'lawyer__name')
    ordering = ('-created_at',)

# Contact Request Admin
@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','lawyer', 'created_at')
    search_fields = ('client_name', 'client_email')
    ordering = ('-created_at',)
