# Generated by Django 4.0.4 on 2022-05-27 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_exam_exammark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exammark',
            options={'verbose_name': 'Экзаменационная отметка', 'verbose_name_plural': 'Экзаменационные   отметки'},
        ),
        migrations.AlterField(
            model_name='exam',
            name='dicipline',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.dicipline', verbose_name='Дисциплина'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.group', verbose_name='Номер группы'),
        ),
        migrations.AlterField(
            model_name='exammark',
            name='exam',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='main.exam', verbose_name='Отметки'),
        ),
        migrations.AlterField(
            model_name='exammark',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_marks', to='main.student', verbose_name='Студент'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота'), (6, 'Воскресенье')], default=0, verbose_name='День недели'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='main.group', verbose_name='Преподаватель')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='main.teacher', verbose_name='Преподаватель')),
            ],
        ),
    ]