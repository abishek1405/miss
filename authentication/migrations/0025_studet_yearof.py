# Generated by Django 4.0.6 on 2022-08-14 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0024_studet'),
    ]

    operations = [
        migrations.AddField(
            model_name='studet',
            name='yearof',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
