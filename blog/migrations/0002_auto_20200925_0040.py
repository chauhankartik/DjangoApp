# Generated by Django 3.0.7 on 2020-09-24 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contetnt',
            new_name='content',
        ),
    ]
