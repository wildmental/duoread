from django.db import models
from app1_user_accounts.models import UserAccount
# Create your models here.


class Message(models.Model):
    """messages pool"""
    msg_title = models.CharField(
        max_length=64,
        verbose_name='doc_title',
        default='doc_title'
    )
    msg_txt = models.CharField(
        max_length=400,
        verbose_name='memo_text',
        default=''
    )
    msg_code = models.CharField(
        max_length=64,
        verbose_name='msg_code',
        default=''
    )

    class Meta:
        db_table = 'message'
        verbose_name = "original messge"
        verbose_name_plural = 'message pool'


class MessageLog(models.Model):
    """messages sent"""
    # foreign key field from Messge
    msg_id = models.ForeignKey(
        Message,
        on_delete=models.RESTRICT
    )
    # foreign key field from UserAccount
    user_id = models.ForeignKey(
        UserAccount,
        on_delete=models.RESTRICT
    )
    sent_dt = models.DateTimeField(
        auto_now_add=True,
        verbose_name='sent_datetime'
    )
    view_dt = models.DateTimeField(
        auto_now_add=False,
        verbose_name='viewd_datetime',
        null=True, blank=True
    )

    class Meta:
        db_table = 'message_log'
        verbose_name = "message log"
        verbose_name_plural = 'message logs'
