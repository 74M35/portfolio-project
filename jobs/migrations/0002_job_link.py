# Generated by Django 3.2.7 on 2021-10-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='link',
            field=models.CharField(default='#', max_length=200),
        ),
    ]
