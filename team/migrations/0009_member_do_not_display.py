# Generated by Django 4.1.5 on 2023-03-09 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_remove_member_display_alter_member_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='do_not_display',
            field=models.BooleanField(default=False),
        ),
    ]
