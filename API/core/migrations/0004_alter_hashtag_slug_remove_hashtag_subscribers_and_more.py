# Generated by Django 4.2.11 on 2024-04-03 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile'),
        ('core', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.RemoveField(
            model_name='hashtag',
            name='subscribers',
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.ImageField(upload_to='organization/logo/'),
        ),
        migrations.AddField(
            model_name='hashtag',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscribed_hashtags', to='user.profile'),
        ),
    ]
