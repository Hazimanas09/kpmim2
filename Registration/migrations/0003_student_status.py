# Generated by Django 5.1.3 on 2024-12-20 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default='MP', max_length=3),
        ),
    ]
