# Generated by Django 4.0.4 on 2022-05-30 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_student_options_alter_student_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
