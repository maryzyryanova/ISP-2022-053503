# Generated by Django 4.0.4 on 2022-05-26 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_schedule_marks_mark_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='marks', to='main.student', verbose_name='Студент'),
        ),
    ]
