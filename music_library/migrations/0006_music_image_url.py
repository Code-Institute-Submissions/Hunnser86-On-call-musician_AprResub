# Generated by Django 3.2 on 2022-04-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0005_auto_20220418_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]