# Generated by Django 2.2.2 on 2019-11-08 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micky', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
