"""model for user documents"""
from django.db import models
# from django.core.validators import MinValueValidator
from app4_docs.validators import validate_file_size
from app1_user_accounts.models import UserAccount


def user_doc_file_path(instance, filename):
    """file will be uploaded to MEDIA_ROOT/user_<id>/<filename>"""
    # filename needs to be customized later
    return 'user_{0}/file/{1}'.format(instance.user_id, filename)


def user_doc_img_path(instance, filename):
    """file will be uploaded to MEDIA_ROOT/user_<id>/<filename>"""
    # filename needs to be customized later
    return 'user_{0}/img/{1}'.format(instance.user_id, filename)


class UserDocs(models.Model):
    """User's documents saved here"""

    # a foreign key field from UserAccount
    user_id = models.ForeignKey(UserAccount,
                                on_delete=models.RESTRICT)

    # data fields
    doc_title = models.CharField(
        max_length=64,
        verbose_name='doc_title',
        default='doc_title'
    )
    doc_txt = models.TextField(
        max_length=32,
        verbose_name='doc_text',
        default='doc_text'
    )
    doc_file = models.FileField(
        upload_to=user_doc_file_path,
        verbose_name='doc_file',
        validators=[validate_file_size]
    )
    doc_img = models.ImageField(
        upload_to=user_doc_img_path,
        verbose_name='doc_img',
        validators=[validate_file_size]
    )
    doc_group = models.CharField(
        max_length=64,
        verbose_name='doc_group',
        default='doc_group'
    )

    # datetime
    add_dt = models.DateTimeField(
        auto_now_add=True,
        verbose_name='add_dt'
    )

    def __str__(self):
        return "user no."+str(self.user_id)+"'s language setting"

    class Meta:
        db_table = 'user_docs'
        verbose_name = 'User Document'
        verbose_name_plural = 'User Documents'
