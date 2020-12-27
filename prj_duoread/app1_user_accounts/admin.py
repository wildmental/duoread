"""
Edit the Admin Site From Here
"""
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from app1_user_accounts.forms import RegisterForm
from app1_user_accounts.forms import UserChangeFrom
from app1_user_accounts.models import UserAccount

# Register your models here.


class UserAccountAdimn(BaseUserAdmin):
    """
    Edit UserAccount Data Expression on Admin Site
    """
    form = UserChangeFrom
    add_form = RegisterForm

    list_display = ('id', 'username', 'nickname',
                    'birthdate', 'join_dt', 'password')
    sortable_by = ('id', 'username', 'birthdate', 'join_dt')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Account info', {'fields': ('username', 'nickname', 'password')}),
        ('Personal info', {'fields': ('birthdate',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'nickname',
                       'birthdate', 'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'nickname')
    ordering = ('id',)
    filter_horizontal = ()


admin.site.register(UserAccount, UserAccountAdimn)
admin.site.unregister(Group)
