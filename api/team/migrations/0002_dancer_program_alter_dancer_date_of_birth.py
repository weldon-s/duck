# Generated by Django 4.2.5 on 2023-10-07 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dancer',
            name='program',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='dancer',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
    ]
