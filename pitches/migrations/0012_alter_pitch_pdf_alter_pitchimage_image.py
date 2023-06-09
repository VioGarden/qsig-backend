# Generated by Django 4.1.5 on 2023-03-06 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0011_alter_pitch_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitch',
            name='pdf',
            field=models.FileField(default='Pdfs/None/pdf_default.pdf', upload_to='Pdfs/'),
        ),
        migrations.AlterField(
            model_name='pitchimage',
            name='image',
            field=models.ImageField(default='Images/None/image_default.png', upload_to='Images/'),
        ),
    ]
