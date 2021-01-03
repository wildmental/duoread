from django.contrib import admin
from app2_user_settings.models import LangSetting
from app2_user_settings.models import AppSetting

# Register your models here.


class LangSetAdimn(admin.ModelAdmin):
    """
    Edit Language Setting Data on Admin Site
    """

    list_display = ('id', 'user_id', 'native_lang',
                    'target_lang1', 'target_lang2', 'set_dt')
    fieldsets = (
        ('User info', {'fields': ('user_id',)}),
        ('Language setting', {'fields': ('native_lang',
                                         'target_lang1',
                                         'target_lang2')}),
    )

    search_fields = ('id', 'user_id')
    ordering = ('id',)


admin.site.register(LangSetting, LangSetAdimn)


class AppSetAdimn(admin.ModelAdmin):
    """
    Edit App Setting Data on Admin Site
    """

    list_display = ('id', 'user_id', 'screen_mode',
                    'txt_size', 'dict_size',
                    'notice_on', 'sms_agree', 'email_agree',
                    'set_dt')
    fieldsets = (
        ('User info', {'fields': ('user_id',)}),
        ('App setting', {'fields': ('screen_mode',
                                    'txt_size',
                                    'dict_size')}),
        ('contact setting', {'fields': ('notice_on',
                                        'sms_agree',
                                        'email_agree')}),
    )

    search_fields = ('id', 'user_id')
    ordering = ('id',)


admin.site.register(AppSetting, AppSetAdimn)
