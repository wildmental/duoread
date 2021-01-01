from django.contrib import admin
from app7_dictionary.models import DictCn


class DictCnAdimn(admin.ModelAdmin):
    """
    Edit Chinese Dictionary Data Expression on Admin Site
    """
    list_display = ('id', 'word', 'pronounciation',
                    'definition', 'word_group', 'frequency',
                    'topic_group', 'manage_code')
    ordering = ('id',)


admin.site.register(DictCn, DictCnAdimn)
