# Generated by Django 4.0.3 on 2022-12-29 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0011_alter_question_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(max_length=150),
        ),
    ]