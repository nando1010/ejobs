# Generated by Django 2.2.7 on 2019-11-11 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_benefits',
            new_name='benefits',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_comment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_requeriments',
            new_name='requeriments',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_schedule',
            new_name='schedule',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_urgency',
            new_name='urgency',
        ),
        migrations.RemoveField(
            model_name='job',
            name='active',
        ),
        migrations.AddField(
            model_name='job',
            name='application_isactive',
            field=models.BooleanField(default=True, help_text='Acepta Postulaciones', verbose_name='Application is active'),
        ),
        migrations.AddField(
            model_name='job',
            name='applications_made',
            field=models.PositiveIntegerField(default=0, help_text='Postulaciones realizadas', verbose_name='Aplications made'),
        ),
    ]
