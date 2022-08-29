# Generated by Django 4.0.6 on 2022-07-31 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_facultyattended'),
    ]

    operations = [
        migrations.CreateModel(
            name='pub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sno', models.IntegerField(max_length=40)),
                ('papertitle', models.EmailField(max_length=254)),
                ('Author', models.CharField(max_length=100)),
                ('Journal', models.CharField(max_length=100)),
                ('Indexed', models.CharField(max_length=12)),
                ('Factor', models.CharField(max_length=100)),
                ('Poru', models.CharField(max_length=100)),
                ('ISSN', models.CharField(max_length=100)),
                ('yearofpub', models.DateField(max_length=100)),
                ('TypeofJournal', models.CharField(max_length=100)),
            ],
        ),
    ]
