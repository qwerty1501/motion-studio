# Generated by Django 4.0.3 on 2022-05-01 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0008_alter_ourclient_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ourclient',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
