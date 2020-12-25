"""this is models.py for app3_wordbook """
from django.db import models
from app1_user_accounts.models import UserAccount

# Create your models here.


class WordMemoCn(models.Model):
    """Simple addon upon user wordbook"""
    # a foreign key field from UserAccount
    user_id = models.ForeignKey(
        UserAccount,
        on_delete=models.RESTRICT
    )
    # will be changed as a foreign key from Dictionary
    word_id = models.CharField(
        max_length=64,
        verbose_name='word_id'
    )

    # data field
    memo_txt = models.CharField(
        max_length=64,
        verbose_name='memo_text',
        default=''
    )

    # datetime
    add_dt = models.DateTimeField(
        auto_now_add=True,
        verbose_name='added_datetime'
    )
    # auto now VS auto now add - need to figure out
    update_dt = models.DateTimeField(
        auto_now=True,
        verbose_name='updated_datetime'
    )

    def __str__(self):
        return str(self.user_id)+self.word_id+str(self.memo_txt)

    class Meta:
        db_table = 'wordmemo_cn'
        verbose_name = 'WordMemo'
        verbose_name_plural = 'WordMemos'
