# Generated by Django 3.2.8 on 2021-10-21 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary',
            old_name='done_good_1',
            new_name='donegood',
        ),
        migrations.RenameField(
            model_name='diary',
            old_name='done_good_2',
            new_name='feelgood',
        ),
        migrations.RenameField(
            model_name='diary',
            old_name='done_good_3',
            new_name='makegood',
        ),
        migrations.RenameField(
            model_name='diary',
            old_name='thanks_1',
            new_name='promise',
        ),
        migrations.RenameField(
            model_name='diary',
            old_name='thanks_2',
            new_name='thanks',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='thanks_3',
        ),
    ]
