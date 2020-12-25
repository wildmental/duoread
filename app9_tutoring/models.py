"""this is models.py for app9_tutoring"""
from django.db import models
from app1_user_accounts.models import UserAccount

# Create your models here.


class TutorRequest(models.Model):
    """Maximum 5 words in 1 request."""
    userid = models.ForeignKey(UserAccount,
                               on_delete=models.RESTRICT)
    title = models.CharField(max_length=64,
                             verbose_name='title')
    word1 = models.CharField(max_length=64,
                             verbose_name='word1')
    word2 = models.CharField(max_length=64, blank=True, default=None,
                             verbose_name='word2')
    word3 = models.CharField(max_length=64, blank=True, default=None,
                             verbose_name='word3')
    word4 = models.CharField(max_length=64, blank=True, default=None,
                             verbose_name='word4')
    word5 = models.CharField(max_length=64, blank=True, default=None,
                             verbose_name='word5')
    words_list = models.CharField(max_length=500, blank=True, default=None,
                                  verbose_name='wordlist')
    question_txt = models.TextField(max_length=1024,
                                    verbose_name='question_txt')
    request_dt = models.DateTimeField(auto_now_add=True,
                                      verbose_name='request_dt')

    def __str__(self):
        return 'tutor_req_'+str(self.userid)+str(self.request_dt)

    class Meta:
        db_table = 'tutor_request'
        verbose_name = 'Tutor Request'
        verbose_name_plural = 'Tutor Requests'
