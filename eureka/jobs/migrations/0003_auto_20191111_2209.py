# Generated by Django 2.2.7 on 2019-11-11 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20191111_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='application_isactive',
            new_name='is_active',
        ),
    ]