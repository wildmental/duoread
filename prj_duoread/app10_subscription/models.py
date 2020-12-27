"""model for subscribtion management"""
from django.db import models
from app1_user_accounts.models import UserAccount


class Subscription(models.Model):
    """User subscribtion data"""

    # a foreign key field from UserAccount
    user_id = models.ForeignKey(UserAccount,
                                on_delete=models.RESTRICT)

    # data fields
    subscribtion_type = models.CharField(
        max_length=64,
        verbose_name='subscribtion_type',
        default='subscribtion_type'
    )
    payment_type = models.CharField(
        max_length=64,
        verbose_name='payment_type',
        default='payment_type'
    )

    # boolean fields (agreements)
    auto_extension = models.BooleanField(default=False)

    # datetime
    start_dt = models.DateTimeField(
        auto_now_add=True,
        verbose_name='start_dt'
    )
    end_dt = models.DateTimeField(
        verbose_name='end_dt'
    )

    def __str__(self):
        return "<user no."+str(self.user_id)+":"+self.subscribtion_type+">"

    class Meta:
        db_table = 'subscribtion'
        verbose_name = 'User Document'
        verbose_name_plural = 'User Documents'


class UsageLimits(models.Model):
    """Usage limit data"""

    # admin manage this
    member_grade = models.CharField(
        max_length=64,
        verbose_name='member_grade',
        default='none_payment'
    )
    word_mark_limit = models.IntegerField(
        verbose_name='word_mark_limit',
        default=100)
    word_memo_limit = models.IntegerField(
        verbose_name='word_memo_limit',
        default=100)
    doc_import_limit = models.IntegerField(
        verbose_name='doc_import_limit',
        default=5)
    doc_max_size = models.IntegerField(
        verbose_name='doc_max_size',
        default=10485760)

    def __str__(self):
        return str("<%s limitations: %d/%d/%d/%d>"
                   % (str(self.member_grade), self.word_mark_limit, self.word_memo_limit,
                      self.doc_import_limit, self.doc_max_size))

    class Meta:
        db_table = 'usage_limit'
        verbose_name = 'usage limit level'
        verbose_name_plural = 'usage limit settings'
