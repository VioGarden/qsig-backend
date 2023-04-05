# Generated by Django 4.1.5 on 2023-03-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0012_alter_pitch_pdf_alter_pitchimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitch',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pitchimage',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pitch',
            name='display',
            field=models.BooleanField(default=True),
        ),
    ]