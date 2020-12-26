"""custom validators for document files"""
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_file_size(file):
    """custom file size validator"""
    filesize = file.size

    if filesize > 10485760:
        raise ValidationError(
            # _("The maximum file size that can be uploaded is 10MB")
            _("최대 10MB까지 업로드할 수 있습니다.")
        )
    else:
        return file
