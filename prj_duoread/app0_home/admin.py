from django.contrib import admin
from app0_home.models import Mailing
# Register your models here.


class MailingAdmin(admin.ModelAdmin):
    """wordbook in admin"""
    list_display = ('email', 'enroll_dt')
    ordering = ('id',)


admin.site.register(Mailing, MailingAdmin)
