"""
Edit the Admin Site From Here
"""
from django.contrib import admin
from .models import WordMemoCn

# Register your models here.


class WordmemoCnAdimn(admin.ModelAdmin):
    """
    Edit Wordmemo Data Expression on Admin Site
    """
    list_display = ('id', 'user_id', 'word_id',
                    'memo_txt', 'add_dt', 'update_dt')
    ordering = ('id',)


admin.site.register(WordMemoCn, WordmemoCnAdimn)
