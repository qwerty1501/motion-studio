# Generated by Django 4.0.3 on 2022-03-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motionApp', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='createstaff',
            name='url_linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='Укажите сылку на ваш linkedin (*Не обязательно)'),
        ),
    ]
