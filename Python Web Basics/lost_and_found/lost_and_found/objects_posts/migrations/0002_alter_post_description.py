# Generated by Django 3.2.3 on 2021-09-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects_posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
