# Generated by Django 4.0.6 on 2022-08-16 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0026_bookpub_fill'),
    ]

    operations = [
        migrations.CreateModel(
            name='infor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val', models.CharField(max_length=4000)),
            ],
        ),
    ]
