# Generated by Django 4.0.3 on 2022-03-27 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_decription_alter_project_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='decription',
            new_name='description',
        ),
    ]