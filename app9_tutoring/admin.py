"""
Edit the Admin Site From Here
"""
from django.contrib import admin
from .models import TutorRequest

# Register your models here.


class TutorRequestAdmin(admin.ModelAdmin):
    """Edit Tutoring request data in Admin site from here"""
    list_display = ('id', 'userid', 'title', 'question_txt', 'request_dt')


admin.site.register(TutorRequest, TutorRequestAdmin)
