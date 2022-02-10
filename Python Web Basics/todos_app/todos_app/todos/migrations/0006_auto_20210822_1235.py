# Generated by Django 3.2.6 on 2021-08-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_auto_20210811_2220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Home', 'Home stuff'), ('Work', 'Work stuff')], max_length=25),
        ),
    ]
