# Generated by Django 3.2.7 on 2021-09-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_auto_20210911_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_Id',
            field=models.EmailField(max_length=254),
        ),
    ]
