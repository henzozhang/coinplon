# Generated by Django 4.1.2 on 2022-10-12 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0003_rename_text_flexpage_apropos_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flexpage',
            old_name='apropos_text',
            new_name='text',
        ),
    ]