# Generated by Django 4.0.3 on 2022-12-29 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0010_alter_profile_operate_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.CharField(max_length=300),
        ),
    ]
