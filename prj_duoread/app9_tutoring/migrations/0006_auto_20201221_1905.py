# Generated by Django 3.1.4 on 2020-12-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app9_tutoring', '0005_auto_20201217_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorrequest',
            name='question_txt',
            field=models.TextField(max_length=1024, verbose_name='question_txt'),
        ),
        migrations.AlterField(
            model_name='tutorrequest',
            name='request_dt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='request_dt'),
        ),
        migrations.AlterField(
            model_name='tutorrequest',
            name='title',
            field=models.CharField(max_length=64, verbose_name='title'),
        ),
    ]
