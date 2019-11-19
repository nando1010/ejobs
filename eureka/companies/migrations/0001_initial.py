# Generated by Django 2.2.7 on 2019-11-19 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('name', models.CharField(help_text='Company Sector name', max_length=100, unique=True, verbose_name='Sector name')),
                ('description', models.TextField(blank=True, help_text='Description', verbose_name='Sector description')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('name', models.CharField(max_length=200, verbose_name='razon social')),
                ('ruc', models.CharField(max_length=11, unique=True)),
                ('trade_name', models.CharField(blank=True, max_length=100, verbose_name='nombre comercial')),
                ('description', models.TextField(blank=True, null=True)),
                ('logo_url', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='company active')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Sector')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]