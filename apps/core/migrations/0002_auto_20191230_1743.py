# Generated by Django 2.1 on 2019-12-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='type',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lname',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='name'),
        ),
    ]