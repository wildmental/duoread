"""Model for app7_dictionary"""
from django.db import models

# Create your models here.


class DictCn(models.Model):
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
    definition = models.TextField(
        max_length=450,
        verbose_name='definition',
        default=''
    )
    word_group = models.CharField(
        max_length=64,
        verbose_name='word_group',
        default='',
        null=True, blank=True
    )
    frequency = models.CharField(
        max_length=64,
        verbose_name='frequency',
        default='',
        null=True, blank=True
    )
    topic_group = models.CharField(
        max_length=64,
        verbose_name='topic_group',
        default='',
        null=True, blank=True
    )
    manage_code = models.CharField(
        max_length=64,
        verbose_name='manage_code',
        default='',
        null=True, blank=True
    )

    def __str__(self):
        return 'Word: '+str(self.id)+'/'+self.word

    class Meta:
        db_table = 'dict_cn'
        verbose_name = 'Word : Chinese'
        verbose_name_plural = 'Dictionary : Chinese'


class DictEn(models.Model):
    """English Dictionary : base data for all the words"""
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
    definition = models.TextField(
        max_length=450,
        verbose_name='definition',
        default=''
    )
    word_group = models.CharField(
        max_length=64,
        verbose_name='word_group',
        default='',
        null=True, blank=True
    )
    frequency = models.CharField(
        max_length=64,
        verbose_name='frequency',
        default='',
        null=True, blank=True
    )
    topic_group = models.CharField(
        max_length=64,
        verbose_name='topic_group',
        default='',
        null=True, blank=True
    )
    manage_code = models.CharField(
        max_length=64,
        verbose_name='manage_code',
        default='',
        null=True, blank=True
    )

    def __str__(self):
        return 'Word: '+str(self.id)+'/'+self.word

    class Meta:
        db_table = 'dict_en'
        verbose_name = 'Word : English'
        verbose_name_plural = 'Dictionary : English'
