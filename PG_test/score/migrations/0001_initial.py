# Generated by Django 2.2.7 on 2019-11-27 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('professor', models.ForeignKey(blank=True, db_column='professor_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='professor.Professor')),
                ('student', models.ForeignKey(blank=True, db_column='student_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
