# Generated by Django 2.2.6 on 2019-11-20 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191119_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='spotify_username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
