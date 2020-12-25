"""
Models Belongs to app2_user_settings
"""
from django.db import models
from app1_user_accounts.models import UserAccount

# Create your models here.


class UserLanguage(models.Model):
    """UserLanguages setting"""

    # a foreign key field from UserAccount
    user_id = models.ForeignKey(UserAccount,
                                on_delete=models.RESTRICT)

    # data fields
    native_lang = models.CharField(
        max_length=32,
        verbose_name='native_lang',
        default='native_lang'
    )
    target_lang1 = models.CharField(
        max_length=32,
        verbose_name='target_lang1',
        default='target_lang1'
    )
    target_lang2 = models.CharField(
        max_length=32,
        verbose_name='target_lang2',
        default=None,
        null=True, blank=True
    )

    # datetime
    set_dt = models.DateTimeField(
        auto_now_add=True,
        verbose_name='set_dt'
    )

    def __str__(self):
        return "user no"+str(self.user_id)+"'s language setting"

    class Meta:
        db_table = 'user_languages'
        verbose_name = 'User Language'
        verbose_name_plural = 'User Languages'
