# Generated by Django 3.1.4 on 2020-12-26 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app7_dictionary', '0001_initial'),
        ('app3_wordbook', '0004_auto_20201226_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmemocn',
            name='word_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app7_dictionary.dictionarycn'),
        ),
    ]
