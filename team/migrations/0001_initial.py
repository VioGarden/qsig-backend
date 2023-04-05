# Generated by Django 4.1.5 on 2023-03-05 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('headshot', models.ImageField(blank=True, default='Headshots/None/temp.jpeg', null=True, upload_to='Headshots/')),
                ('year', models.CharField(blank=True, choices=[('', '----------'), ('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year'), ('Undergraduate', 'Undergraduate'), ('Graduate', 'Graduate'), ('Alumni', 'Alumni')], default='Undergraduate', max_length=15, null=True)),
                ('vertical', models.CharField(blank=True, choices=[('', '----------'), ('Industrials', 'Industrials'), ('Technology, Media & Telecom', 'Technology, Media & Telecom'), ('Consumers & Healthcare', 'Consumers & Healthcare'), ('Energy & Commodities', 'Energy & Commodities'), ('Finance, Insurance & Real Estate', 'Finance, Insurance & Real Estate'), ('Market & Trends', 'Market & Trends'), ('Analytics', 'Analytics'), ('Commodities', 'Commodities'), ('Consumers', 'Consumers'), ('Energy', 'Energy'), ('Finance', 'Finance'), ('Healthcare', 'Healthcare'), ('Insurance', 'Insurance'), ('Market', 'Market'), ('Media', 'Media'), ('Real Estate', 'Real Estate'), ('Technology', 'Technology'), ('Telecom', 'Telecom'), ('Trends', 'Trends')], default='', max_length=100, null=True)),
                ('custom_vertical', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=250, null=True)),
                ('linked_in', models.URLField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]