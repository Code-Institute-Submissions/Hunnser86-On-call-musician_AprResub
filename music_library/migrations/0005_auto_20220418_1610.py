# Generated by Django 3.2 on 2022-04-18 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0004_auto_20220418_1601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={},
        ),
        migrations.AddField(
            model_name='music',
            name='description',
            field=models.TextField(default='description', max_length=400),
        ),
    ]
