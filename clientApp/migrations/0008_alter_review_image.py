# Generated by Django 3.2.9 on 2022-05-28 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0007_alter_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(upload_to='image/client', verbose_name='Фотография'),
        ),
    ]
