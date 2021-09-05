# Generated by Django 3.1.7 on 2021-09-05 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=15, verbose_name='课程ID')),
                ('course_name', models.CharField(max_length=30, verbose_name='课程名称')),
                ('grade', models.IntegerField(default=60, verbose_name='分数')),
            ],
            options={
                'db_table': 'course',
            },
        ),
    ]
