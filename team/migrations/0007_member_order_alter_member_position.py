# Generated by Django 4.1.5 on 2023-03-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_alter_member_headshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='position',
            field=models.CharField(blank=True, choices=[('Co-Chair', 'Co-Chair'), ('PM/Director', 'PM/Director'), ('Senior Investment Analyst', 'Senior Investment Analyst'), ('Junior Investment Analyst', 'Junior Investment Analyst'), ('Team Photo', 'Team Photo')], max_length=30, null=True),
        ),
    ]
