from django.db import models

# Create your models here.


class Mailing(models.Model):
    """UserAccount basic"""

    # data fields
    email = models.EmailField(
        max_length=32,
        verbose_name='email',
        default='email',
        unique=True
    )
    # datetime
    enroll_dt = models.DateTimeField(
        auto_now_add=True,
        verbose_name='join_dt'
    )

    class Meta:
        db_table = 'mailing'
        verbose_name = 'Mailing Enroll'
        verbose_name_plural = 'Mailing List'
