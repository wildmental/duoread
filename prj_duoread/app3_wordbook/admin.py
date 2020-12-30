"""
Edit the Admin Site From Here
"""
from django.contrib import admin
from app3_wordbook.models import UserWordsCn

# Register your models here.


class WordBookCnAdmin(admin.ModelAdmin):
    """wordbook in admin"""
    list_display = ('id', 'user_id', 'word_id',
                    'word_mark', 'add_dt', 'update_dt')
    ordering = ('id',)


admin.site.register(UserWordsCn, WordBookCnAdmin)
