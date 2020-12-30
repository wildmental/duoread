"""
Models Belongs to app1_user_accounts
"""
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import _user_has_perm
from django.contrib.auth.models import _user_has_module_perms
from django.contrib.auth.models import AbstractBaseUser


class UserManager(BaseUserManager):
    """user manager class"""

    def _create_user(self, username, nickname, password, birthdate=None, **extra_fields):
        """called by create_user()"""
        username = self.normalize_email(username)
        nickname = self.model.normalize_username(nickname)
        user_account = self.model(username=username, nickname=nickname,
                                  birthdate=birthdate, **extra_fields)
        user_account.set_password(password)
        user_account.save(using=self._db)
        return user_account

    def create_user(self, username, nickname, password, birthdate=None, **extra_fields):
        """creating service user"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, nickname, password, birthdate, **extra_fields)

    def create_superuser(self, username, nickname, password):
        """creating management user"""
        superuser_account = self.create_user(
            username=username,
            nickname=nickname,
            password=password
        )
        superuser_account.is_superuser = True
        superuser_account.is_admin = True
        superuser_account.is_staff = True
        superuser_account.is_active = True
        superuser_account.save(using=self._db)
        return superuser_account


class UserAccount(AbstractBaseUser):
    """UserAccount basic"""
    # important fields setting
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']

    # data fields
    username = models.EmailField(
        max_length=32,
        verbose_name='username',
        default='username',
        unique=True
    )
    nickname = models.CharField(
        max_length=32,
        verbose_name='nickname',
        default='nickname'
    )
    password = models.CharField(
        max_length=240,
        verbose_name='password',
        default='password'
    )
    birthdate = models.DateField(
        verbose_name='birth date',
        null=True, blank=True
    )

    # datetime
    join_dt = models.DateTimeField(
        auto_now_add=True,
        verbose_name='join_dt'
    )

    # boolean fields (privileges)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # user manage helper class
    objects = UserManager()

    def __str__(self):
        return '<UserAccount: '+self.username+'>'

    def has_perm(self, perm, obj=None):
        """calls upper perm check"""
        if self.is_active and self.is_superuser:
            return True
        # Otherwise we need to check the backends.
        return _user_has_perm(self, perm, obj)

    def has_module_perms(self, app_label):
        """calls upper module_perm check"""
        if self.is_active and self.is_superuser:
            return True
        return _user_has_module_perms(self, app_label)

    class Meta:
        db_table = 'user_account'
        verbose_name = 'User Account'
        verbose_name_plural = 'User Accounts'
