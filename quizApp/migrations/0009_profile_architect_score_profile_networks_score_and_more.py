# Generated by Django 4.0.3 on 2022-12-17 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0008_rename_question_text1_suggestion_question_suggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='architect_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='networks_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='nummerical_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='operate_score',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='programming_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='signals_score',
            field=models.IntegerField(default=0),
        ),
    ]
