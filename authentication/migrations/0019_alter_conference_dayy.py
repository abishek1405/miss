# Generated by Django 4.0.6 on 2022-08-06 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0018_rename_day_conference_dayy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='dayy',
            field=models.CharField(max_length=14),
        ),
    ]