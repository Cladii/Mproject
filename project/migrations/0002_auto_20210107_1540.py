# Generated by Django 3.1.1 on 2021-01-07 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('project_management', 'Can create, assign and delete project')]},
        ),
    ]