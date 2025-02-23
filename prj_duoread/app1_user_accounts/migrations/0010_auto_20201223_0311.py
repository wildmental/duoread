# Generated by Django 3.1.4 on 2020-12-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1_user_accounts', '0009_auto_20201221_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='email',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='nickname',
            field=models.CharField(default='nickname', max_length=32, verbose_name='nickname'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='password',
            field=models.CharField(default='password', max_length=240, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='username',
            field=models.EmailField(default='username', max_length=32, unique=True, verbose_name='username'),
        ),
    ]
