# Generated by Django 3.2.8 on 2021-11-24 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_diary_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_diary_user_friends_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FriendsApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_from', models.CharField(max_length=199)),
                ('ok_sign', models.BooleanField(default=False)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='friendsapply',
            constraint=models.UniqueConstraint(fields=('user_from', 'user_to'), name='unique apply'),
        ),
    ]