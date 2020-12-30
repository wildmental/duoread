"""this is models.py for app3_wordbook """
from django.db import models
from app1_user_accounts.models import UserAccount
from app7_dictionary.models import DictionaryCn

# Create your models here.


class UserWordsCn(models.Model):
    """User's marked words"""
    # foreign key field from UserAccount
    user_id = models.ForeignKey(
        UserAccount,
        on_delete=models.RESTRICT
    )
    # foreign key field from Dictionary
    word_id = models.ForeignKey(
        DictionaryCn,
        on_delete=models.RESTRICT
    )
    # choice field
    VIEWED = 'V'
    UNKNOWN = 'U'
    KNOWN = 'K'
    CONFUSING = 'C'
    WORD_MARK_CHOICES = [
        (VIEWED, 'Viewed'),
        (UNKNOWN, 'Unknown'),
        (KNOWN, 'Known'),
        (CONFUSING, 'Confusing')
    ]
    word_mark = models.CharField(
        max_length=1,
        verbose_name='word_mark',
        choices=WORD_MARK_CHOICES,
        default=VIEWED,
    )
    # data field
    memo_txt = models.CharField(
        max_length=200,
        verbose_name='memo_text',
        default='',
        null=True, blank=True
    )
    word_context = models.CharField(
        max_length=200,
        verbose_name='word_context',
        default='',
        null=True, blank=True
    )
    # datetime
    add_dt = models.DateTimeField(
        auto_now_add=True,
        verbose_name='added_datetime'
    )
    # auto now VS auto now add - need to figure out
    update_dt = models.DateTimeField(
        auto_now=True,
        verbose_name='updated_datetime',
        null=True, blank=True
    )

    def __str__(self):
        return '<User words:'+str(self.user_id)+'/'+str(self.word_id)+'/'+str(self.word_mark)+'>'

    class Meta:
        db_table = 'userwords_cn'
        verbose_name = "User Marked Word"
        verbose_name_plural = 'User WordBook'
