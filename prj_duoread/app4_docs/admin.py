from django.contrib import admin

# Register your models here.
from app4_docs.models import UserDocs

# Register your models here.


class UserDocsAdmin(admin.ModelAdmin):
    """UserDocs in admin"""
    list_display = ('id', 'user_id', 'doc_title',
                    'doc_text', 'doc_group',
                    'doc_file', 'doc_img',
                    'add_dt')
    ordering = ('id',)


admin.site.register(UserDocs, UserDocsAdmin)
