# Generated by Django 3.2.8 on 2021-11-07 13:53

import diary.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(error_messages={'unique': '이미 사용중인 닉네임입니다.'}, max_length=15, null=True, unique=True, validators=[diary.validators.validate_no_special_characters]),
        ),
    ]
