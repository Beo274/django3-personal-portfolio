# Generated by Django 4.0.3 on 2022-03-27 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Blogs',
        ),
    ]