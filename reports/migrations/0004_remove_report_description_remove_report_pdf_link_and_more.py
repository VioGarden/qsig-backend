# Generated by Django 4.1.5 on 2023-02-21 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_report_display_reportimage_display'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='description',
        ),
        migrations.RemoveField(
            model_name='report',
            name='pdf_link',
        ),
        migrations.RemoveField(
            model_name='report',
            name='user',
        ),
        migrations.AddField(
            model_name='report',
            name='pdf',
            field=models.FileField(default='Pdfs/None/No0pdf.pdf', upload_to='Pdfs/'),
        ),
    ]
