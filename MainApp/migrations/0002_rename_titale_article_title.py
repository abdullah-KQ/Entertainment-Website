# Generated by Django 4.1.5 on 2023-06-27 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='titale',
            new_name='title',
        ),
    ]
