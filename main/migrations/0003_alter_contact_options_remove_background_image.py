# Generated by Django 5.1.2 on 2024-10-29 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_background_contact_alter_banner_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Kontakt', 'verbose_name_plural': 'Kontaktlar'},
        ),
        migrations.RemoveField(
            model_name='background',
            name='image',
        ),
    ]
