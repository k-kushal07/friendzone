# Generated by Django 2.1 on 2021-05-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
