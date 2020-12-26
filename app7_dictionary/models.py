"""Model for app7_dictionary"""
from django.db import models

# Create your models here.


class DictionaryCn(models.Model):
    """Chinese Dictionary : base data for all the words"""
    word = models.CharField(
        max_length=64,
        verbose_name='word',
        default=''
    )
    pronounciation = models.CharField(
        max_length=64,
        verbose_name='pronounciation',
        default='',
        null=True
    )
    definition = models.CharField(
        max_length=64,
        verbose_name='definition',
        default=''
    )
    word_group = models.CharField(
        max_length=64,
        verbose_name='word_group',
        default='',
        null=True
    )
    frequency = models.CharField(
        max_length=64,
        verbose_name='frequency',
        default='',
        null=True
    )
    topic_group = models.CharField(
        max_length=64,
        verbose_name='topic_group',
        default='',
        null=True
    )
    manage_code = models.CharField(
        max_length=64,
        verbose_name='manage_code',
        default=''
    )

    def __str__(self):
        return 'Word :'+str(self.id)+'/'+self.word

    class Meta:
        db_table = 'dictionary_cn'
        verbose_name = 'Word : Chinese'
        verbose_name_plural = 'Dictionary : Chinese'
