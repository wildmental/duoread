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

    # data field
    word_mark = models.CharField(
        max_length=64,
        verbose_name='word_mark',
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
        return 'User words:'+str(self.user_id)+'/'+self.word_id+'/'+str(self.word_mark)

    class Meta:
        db_table = 'userwords_cn'
        verbose_name = "user's word mark"
        verbose_name_plural = 'user wordbook'


class WordMemoCn(models.Model):
    """Simple addon upon user wordbook"""
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

    # data field
    memo_txt = models.CharField(
        max_length=100,
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
        return 'Word memo:'+str(self.user_id)+'/'+self.word_id+'/'+str(self.memo_txt)

    class Meta:
        db_table = 'wordmemo_cn'
        verbose_name = 'WordMemo'
        verbose_name_plural = 'WordMemos'
