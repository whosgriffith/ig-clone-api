# Generated by Django 3.1.13 on 2021-09-03 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210903_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'get_latest_by': 'created', 'ordering': ['-created', '-modified']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'get_latest_by': 'created', 'ordering': ['-created', '-modified']},
        ),
    ]
