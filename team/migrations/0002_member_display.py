# Generated by Django 4.1.5 on 2023-03-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='display',
            field=models.BooleanField(default=True),
        ),
    ]