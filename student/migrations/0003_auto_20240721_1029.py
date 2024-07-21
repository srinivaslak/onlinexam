# Generated by Django 3.0.5 on 2024-07-21 04:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='branch',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sid',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
    ]
